import json
from pathlib import Path
from typing import Any
from ticket_booking.config import DATA_DIR, USERS_FILE, EVENTS_FILE, BOOKINGS_FILE

class FileStorage:
    def __init__(self, base_dir: str | Path | None = None) -> None:
        self.base_dir = Path(base_dir) if base_dir is not None else Path(DATA_DIR)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        # Ensure files exist
        for fn in (USERS_FILE, EVENTS_FILE, BOOKINGS_FILE):
            p = self.base_dir / fn
            if not p.exists():
                p.write_text("[]", encoding="utf-8")

    def _path(self, filename: str) -> Path:
        return self.base_dir / filename

    def load_list(self, filename: str) -> list[dict[str, Any]]:
        p = self._path(filename)
        try:
            return json.loads(p.read_text(encoding="utf-8") or "[]")
        except json.JSONDecodeError:
            return []

    def save_list(self, filename: str, items: list[dict[str, Any]]) -> None:
        p = self._path(filename)
        p.write_text(json.dumps(items, indent=2), encoding="utf-8")
