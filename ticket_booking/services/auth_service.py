from __future__ import annotations
import hashlib
from ticket_booking.storage.file_storage import FileStorage
from ticket_booking.storage.repositories import UserRepo
from ticket_booking.utils.validators import validate_username, validate_password, validate_role
from ticket_booking.utils.exceptions import ValidationError
from ticket_booking.config import DEFAULT_ADMIN_USERNAME, DEFAULT_ADMIN_PASSWORD

class AuthService:
    def __init__(self, storage: FileStorage) -> None:
        self.repo = UserRepo(storage)
        self._ensure_default_admin()

    def _hash(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def _ensure_default_admin(self) -> None:
        users = self.repo.all()
        if not any(u.get("username") == DEFAULT_ADMIN_USERNAME for u in users):
            users.append({
                "username": DEFAULT_ADMIN_USERNAME,
                "password_hash": self._hash(DEFAULT_ADMIN_PASSWORD),
                "role": "admin",
            })
            self.repo.save_all(users)

    def register(self, username: str, password: str, role: str = "user") -> dict:
        try:
            validate_username(username)
            validate_password(password)
            validate_role(role)
            users = self.repo.all()
            if any(u.get("username") == username for u in users):
                return {"success": False, "message": "Duplicate user."}
            users.append({"username": username, "password_hash": self._hash(password), "role": role})
            self.repo.save_all(users)
            return {"success": True, "message": "Registration successful."}
        except ValidationError as e:
            return {"success": False, "message": str(e)}

    def login(self, username: str, password: str) -> dict:
        try:
            validate_username(username)
            users = self.repo.all()
            user = next((u for u in users if u.get("username") == username), None)
            if user is None:
                return {"success": False, "message": "Unknown user."}
            if user.get("password_hash") != self._hash(password):
                return {"success": False, "message": "Wrong password."}
            return {"success": True, "message": "Login successful.", "role": user.get("role", "user")}
        except ValidationError as e:
            return {"success": False, "message": str(e)}
