import pytest

# White-box: Path coverage for BookingService

@pytest.mark.whitebox
def test_book_event_not_found_path(booking_service_fixture):
    result = booking_service_fixture.book(event_id="E404", username="user", quantity=1)
    assert result["success"] is False

@pytest.mark.whitebox
def test_book_capacity_insufficient_path(event_service_fixture, booking_service_fixture):
    ev = event_service_fixture.create_event("Show", "2026-02-01", "Arena", 1, 40.0, "Drama")
    event_id = ev["event_id"]
    r1 = booking_service_fixture.book(event_id=event_id, username="u1", quantity=1)
    r2 = booking_service_fixture.book(event_id=event_id, username="u2", quantity=1)
    assert r1["success"] is True
    assert r2["success"] is False
