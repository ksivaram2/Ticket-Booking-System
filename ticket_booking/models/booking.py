from dataclasses import dataclass

@dataclass
class Booking:
    booking_id: str
    event_id: str
    username: str
    quantity: int
    total_price: float
    status: str = "active"
