import pytest

# Symbolic: executable checks mapped to documented constraints

@pytest.mark.symbolic
def test_symbolic_booking_success(event_service_fixture, booking_service_fixture):
    ev = event_service_fixture.create_event("SymShow", "2026-02-01", "Arena", 5, 10.0, "Drama")
    res = booking_service_fixture.book(ev["event_id"], "u", 2)
    assert res["success"] is True
