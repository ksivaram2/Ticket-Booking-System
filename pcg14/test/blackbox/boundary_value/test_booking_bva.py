import pytest

# Black-box: Boundary Value Analysis for BookingService (quantity)

@pytest.mark.blackbox
def test_book_quantity_min(event_service_fixture, booking_service_fixture):
    ev = event_service_fixture.create_event("Match", "2026-03-01", "Stadium", 10, 25.0, "Sports")
    event_id = ev["event_id"]
    result = booking_service_fixture.book(event_id=event_id, username="user", quantity=1)
    assert result["success"] is True

@pytest.mark.blackbox
def test_book_quantity_zero_invalid(event_service_fixture, booking_service_fixture):
    ev = event_service_fixture.create_event("Match", "2026-03-01", "Stadium", 10, 25.0, "Sports")
    event_id = ev["event_id"]
    result = booking_service_fixture.book(event_id=event_id, username="user", quantity=0)
    assert result["success"] is False
