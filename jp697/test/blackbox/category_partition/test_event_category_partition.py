import pytest

# Black-box: Category Partition for EventService

@pytest.mark.blackbox
def test_create_event_valid(event_service_fixture):
    svc = event_service_fixture
    result = svc.create_event(
        name="Concert",
        date="2026-02-10",
        venue="Hall A",
        capacity=100,
        base_price=50.0,
        category="Music"
    )
    assert result["success"] is True

@pytest.mark.blackbox
def test_create_event_invalid_capacity(event_service_fixture):
    svc = event_service_fixture
    result = svc.create_event(
        name="Concert",
        date="2026-02-10",
        venue="Hall A",
        capacity=-1,
        base_price=50.0,
        category="Music"
    )
    assert result["success"] is False
