from __future__ import annotations
from typing import Any
from ticket_booking.storage.file_storage import FileStorage
from ticket_booking.storage.repositories import EventRepo, BookingRepo
from ticket_booking.utils.validators import validate_event_fields
from ticket_booking.utils.exceptions import ValidationError
from ticket_booking.utils.id_generator import generate_id

class EventService:
    def __init__(self, storage: FileStorage) -> None:
        self.events = EventRepo(storage)
        self.bookings = BookingRepo(storage)

    def create_event(self, name: str, date: str, venue: str, capacity: int, base_price: float, category: str) -> dict:
        try:
            validate_event_fields(name, date, venue, capacity, float(base_price), category)
            ev_id = generate_id("E")
            items = self.events.all()
            items.append({
                "event_id": ev_id,
                "name": name,
                "date": date,
                "venue": venue,
                "capacity": int(capacity),
                "base_price": float(base_price),
                "category": category
            })
            self.events.save_all(items)
            return {"success": True, "message": "Event created.", "event_id": ev_id}
        except (ValidationError, ValueError) as e:
            return {"success": False, "message": str(e)}

    def update_event(self, event_id: str, updates: dict[str, Any]) -> dict:
        items = self.events.all()
        idx = next((i for i, e in enumerate(items) if e.get("event_id") == event_id), None)
        if idx is None:
            return {"success": False, "message": "Event not found."}
        # Apply updates with minimal validation
        ev = items[idx]
        for k, v in updates.items():
            if k == "capacity":
                try:
                    v = int(v)
                except ValueError:
                    return {"success": False, "message": "Invalid capacity."}
                if v <= 0:
                    return {"success": False, "message": "Capacity must be positive."}
            if k == "base_price":
                v = float(v)
                if v < 0:
                    return {"success": False, "message": "Base price must be non-negative."}
            ev[k] = v
        items[idx] = ev
        self.events.save_all(items)
        return {"success": True, "message": "Event updated."}

    def delete_event(self, event_id: str) -> dict:
        # Dependency check: active bookings exist?
        bookings = self.bookings.all()
        if any(b.get("event_id") == event_id and b.get("status") == "active" for b in bookings):
            return {"success": False, "message": "Event has active bookings."}
        items = self.events.all()
        new_items = [e for e in items if e.get("event_id") != event_id]
        if len(new_items) == len(items):
            return {"success": False, "message": "Event not found."}
        self.events.save_all(new_items)
        return {"success": True, "message": "Event deleted."}

    def get_event(self, event_id: str) -> dict | None:
        return next((e for e in self.events.all() if e.get("event_id") == event_id), None)

    def reduce_capacity(self, event_id: str, qty: int) -> bool:
        items = self.events.all()
        for i, e in enumerate(items):
            if e.get("event_id") == event_id:
                if e.get("capacity", 0) >= qty:
                    e["capacity"] = int(e["capacity"]) - qty
                    items[i] = e
                    self.events.save_all(items)
                    return True
                return False
        return False

    def increase_capacity(self, event_id: str, qty: int) -> None:
        items = self.events.all()
        for i, e in enumerate(items):
            if e.get("event_id") == event_id:
                e["capacity"] = int(e.get("capacity", 0)) + qty
                items[i] = e
                self.events.save_all(items)
                return
    def list_events(self) -> list[dict]:
        return self.events.all()

    def search_events(self, keyword: str) -> list[dict]:
        k = (keyword or "").strip().lower()
        if not k:
            return self.events.all()

        results = []
        for e in self.events.all():
            hay = " ".join(
                [
                    str(e.get("name", "")),
                    str(e.get("category", "")),
                    str(e.get("venue", "")),
                    str(e.get("date", "")),
                    str(e.get("event_id", "")),
                ]
            ).lower()
            if k in hay:
                results.append(e)
        return results
