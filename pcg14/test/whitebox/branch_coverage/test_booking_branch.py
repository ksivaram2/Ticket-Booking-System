import pytest

# White-box: Branch coverage for BookingService

@pytest.mark.whitebox
def test_cancel_not_found_branch(booking_service_fixture):
    res = booking_service_fixture.cancel("B404")
    assert res["success"] is False
