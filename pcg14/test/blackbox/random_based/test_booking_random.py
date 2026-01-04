import pytest
import random

# Black-box: Random based booking quantities

@pytest.mark.blackbox
def test_random_booking_quantities(event_service_fixture, booking_service_fixture):
    ev = event_service_fixture.create_event("Show", "2026-02-01", "Arena", 20, 40.0, "Drama")
    event_id = ev["event_id"]
    for _ in range(10):
        qty = random.randint(1, 3)
        res = booking_service_fixture.book(event_id=event_id, username="u", quantity=qty)
        assert "success" in res
