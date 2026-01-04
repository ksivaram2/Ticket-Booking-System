import pytest

# Black-box: Category Partition for BookingService

@pytest.mark.blackbox
def test_booking_event_not_found(booking_service_fixture):
    res = booking_service_fixture.book(event_id="E404", username="user", quantity=1)
    assert res["success"] is False
