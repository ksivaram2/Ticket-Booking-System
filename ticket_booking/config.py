from pathlib import Path

# Default data directory (can be overridden in FileStorage for testing)
DATA_DIR = Path(__file__).resolve().parent / "data"

USERS_FILE = "users.json"
EVENTS_FILE = "events.json"
BOOKINGS_FILE = "bookings.json"

DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "AdminPass123"
