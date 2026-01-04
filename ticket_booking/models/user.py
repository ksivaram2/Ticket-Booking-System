from dataclasses import dataclass

@dataclass
class User:
    username: str
    password_hash: str
    role: str = "user"
