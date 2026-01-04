from dataclasses import dataclass

@dataclass
class Event:
    event_id: str
    name: str
    date: str
    venue: str
    capacity: int
    base_price: float
    category: str
