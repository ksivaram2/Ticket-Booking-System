from ticket_booking.services.auth_service import AuthService
from ticket_booking.services.event_service import EventService
from ticket_booking.services.booking_service import BookingService
from ticket_booking.services.report_service import ReportService
from ticket_booking.storage.file_storage import FileStorage


class CLIController:
    def __init__(self) -> None:
        storage = FileStorage()
        self.auth = AuthService(storage)
        self.events = EventService(storage)
        self.bookings = BookingService(storage, self.events, self.auth)
        self.reports = ReportService(storage)
        self.current_user: dict | None = None  # {"username": str, "role": str}

    def is_logged_in(self) -> bool:
        return self.current_user is not None

    def logout(self) -> None:
        self.current_user = None

    def register(self, username: str, password: str) -> dict:
        return self.auth.register(username=username, password=password, role="user")

    def login(self, username: str, password: str) -> dict:
        res = self.auth.login(username=username, password=password)
        if res.get("success"):
            self.current_user = {"username": username, "role": res.get("role", "user")}
        return res

    def require_login(self) -> dict:
        if not self.current_user:
            return {"success": False, "message": "Please login first."}
        return {"success": True}

    def require_admin(self) -> dict:
        chk = self.require_login()
        if not chk["success"]:
            return chk
        if self.current_user.get("role") != "admin":
            return {"success": False, "message": "Admin access required."}
        return {"success": True}
