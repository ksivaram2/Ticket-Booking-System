from __future__ import annotations
from typing import Any
from ticket_booking.storage.file_storage import FileStorage
from ticket_booking.storage.repositories import EventRepo, BookingRepo

class ReportService:
    def __init__(self, storage: FileStorage) -> None:
        self.events = EventRepo(storage)
        self.bookings = BookingRepo(storage)

    def total_revenue_by_event(self) -> dict[str, float]:
        revenue: dict[str, float] = {}
        for b in self.bookings.all():
            if b.get("status") != "active":
                continue
            eid = b.get("event_id")
            revenue[eid] = revenue.get(eid, 0.0) + float(b.get("total_price", 0.0))
        return revenue

    def occupancy_rates(self) -> dict[str, float]:
        # Occupancy rate = booked seats / (booked seats + remaining capacity)
        # Since we store only remaining capacity, compute booked seats from bookings list.
        events = {e["event_id"]: e for e in self.events.all()}
        booked: dict[str, int] = {}
        for b in self.bookings.all():
            if b.get("status") == "active":
                booked[b["event_id"]] = booked.get(b["event_id"], 0) + int(b.get("quantity", 0))
        rates: dict[str, float] = {}
        for eid, e in events.items():
            remaining = int(e.get("capacity", 0))
            used = booked.get(eid, 0)
            denom = used + remaining
            rates[eid] = round((used / denom) if denom > 0 else 0.0, 4)
        return rates
