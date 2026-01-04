import pytest

# Black-box: Boundary Value Analysis for EventService

@pytest.mark.blackbox
def test_create_event_capacity_min_valid(event_service_fixture):
    svc = event_service_fixture
    result = svc.create_event("Expo", "2026-02-12", "Hall B", 1, 10.0, "Tech")
    assert result["success"] is True

@pytest.mark.blackbox
def test_create_event_capacity_zero_invalid(event_service_fixture):
    svc = event_service_fixture
    result = svc.create_event("Expo", "2026-02-12", "Hall B", 0, 10.0, "Tech")
    assert result["success"] is False
