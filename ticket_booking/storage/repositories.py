from __future__ import annotations
from typing import Any
from ticket_booking.storage.file_storage import FileStorage
from ticket_booking.config import USERS_FILE, EVENTS_FILE, BOOKINGS_FILE

class UserRepo:
    def __init__(self, storage: FileStorage) -> None:
        self.storage = storage

    def all(self) -> list[dict[str, Any]]:
        return self.storage.load_list(USERS_FILE)

    def save_all(self, users: list[dict[str, Any]]) -> None:
        self.storage.save_list(USERS_FILE, users)

class EventRepo:
    def __init__(self, storage: FileStorage) -> None:
        self.storage = storage

    def all(self) -> list[dict[str, Any]]:
        return self.storage.load_list(EVENTS_FILE)

    def save_all(self, events: list[dict[str, Any]]) -> None:
        self.storage.save_list(EVENTS_FILE, events)

class BookingRepo:
    def __init__(self, storage: FileStorage) -> None:
        self.storage = storage

    def all(self) -> list[dict[str, Any]]:
        return self.storage.load_list(BOOKINGS_FILE)

    def save_all(self, bookings: list[dict[str, Any]]) -> None:
        self.storage.save_list(BOOKINGS_FILE, bookings)
