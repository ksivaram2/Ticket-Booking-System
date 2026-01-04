import pytest

# Concolic: concrete tests derived from constraints

@pytest.mark.concolic
def test_concolic_capacity_insufficient(event_service_fixture, booking_service_fixture):
    ev = event_service_fixture.create_event("Show", "2026-02-01", "Arena", 1, 40.0, "Drama")
    event_id = ev["event_id"]
    booking_service_fixture.book(event_id=event_id, username="u1", quantity=1)
    r2 = booking_service_fixture.book(event_id=event_id, username="u2", quantity=1)
    assert r2["success"] is False
