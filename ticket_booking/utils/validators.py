from ticket_booking.utils.exceptions import ValidationError
from ticket_booking.utils.date_utils import is_iso_date

def validate_username(username: str) -> None:
    if not username or len(username.strip()) == 0:
        raise ValidationError("Username must not be empty.")
    if len(username) > 20:
        raise ValidationError("Username too long.")

def validate_password(password: str) -> None:
    if not password or len(password) < 8:
        raise ValidationError("Password must be at least 8 characters.")

def validate_role(role: str) -> None:
    if role not in ("user", "admin"):
        raise ValidationError("Invalid role.")

def validate_event_fields(name: str, date: str, venue: str, capacity: int, base_price: float, category: str) -> None:
    if not name.strip():
        raise ValidationError("Event name must not be empty.")
    if not is_iso_date(date):
        raise ValidationError("Date must be in YYYY-MM-DD format.")
    if not venue.strip():
        raise ValidationError("Venue must not be empty.")
    if capacity <= 0:
        raise ValidationError("Capacity must be positive.")
    if base_price < 0:
        raise ValidationError("Base price must be non-negative.")
    if not category.strip():
        raise ValidationError("Category must not be empty.")

def validate_quantity(qty: int) -> None:
    if qty <= 0:
        raise ValidationError("Quantity must be positive.")
