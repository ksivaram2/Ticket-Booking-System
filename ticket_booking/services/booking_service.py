from __future__ import annotations
from ticket_booking.storage.file_storage import FileStorage
from ticket_booking.storage.repositories import BookingRepo
from ticket_booking.utils.validators import validate_quantity
from ticket_booking.utils.exceptions import ValidationError
from ticket_booking.utils.id_generator import generate_id
from ticket_booking.services.pricing_service import PricingService
from ticket_booking.services.event_service import EventService
from ticket_booking.services.auth_service import AuthService

class BookingService:
    def __init__(self, storage: FileStorage, event_service: EventService, auth_service: AuthService) -> None:
        self.repo = BookingRepo(storage)
        self.events = event_service
        self.auth = auth_service
        self.pricing = PricingService()

    def book(self, event_id: str, username: str, quantity: int) -> dict:
        try:
            validate_quantity(int(quantity))
            ev = self.events.get_event(event_id)
            if ev is None:
                return {"success": False, "message": "Event not found."}
            qty = int(quantity)
            if not self.events.reduce_capacity(event_id, qty):
                return {"success": False, "message": "Insufficient capacity."}
            total = self.pricing.calculate_total(float(ev.get("base_price", 0.0)), qty)
            booking_id = generate_id("B")
            items = self.repo.all()
            items.append({
                "booking_id": booking_id,
                "event_id": event_id,
                "username": username,
                "quantity": qty,
                "total_price": total,
                "status": "active"
            })
            self.repo.save_all(items)
            return {"success": True, "message": "Booking created.", "booking_id": booking_id, "total_price": total}
        except (ValidationError, ValueError) as e:
            return {"success": False, "message": str(e)}

    def cancel(self, booking_id: str) -> dict:
        items = self.repo.all()
        for i, b in enumerate(items):
            if b.get("booking_id") == booking_id:
                if b.get("status") != "active":
                    return {"success": False, "message": "Booking already cancelled."}
                b["status"] = "cancelled"
                items[i] = b
                self.repo.save_all(items)
                # restore capacity
                self.events.increase_capacity(b.get("event_id"), int(b.get("quantity", 0)))
                return {"success": True, "message": "Booking cancelled."}
        return {"success": False, "message": "Booking not found."}
    def list_by_user(self, username: str) -> list[dict]:
        return [b for b in self.repo.all() if b.get("username") == username]

    def list_all(self) -> list[dict]:
        return self.repo.all()
