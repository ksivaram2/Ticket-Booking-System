import pytest

# White-box: Path coverage for EventService (valid update vs invalid update)

@pytest.mark.whitebox
def test_update_capacity_invalid_path(event_service_fixture):
    svc = event_service_fixture
    created = svc.create_event("Expo", "2026-02-12", "Hall B", 50, 20.0, "Tech")
    event_id = created["event_id"]
    res = svc.update_event(event_id, {"capacity": -5})
    assert res["success"] is False

@pytest.mark.whitebox
def test_update_capacity_valid_path(event_service_fixture):
    svc = event_service_fixture
    created = svc.create_event("Expo2", "2026-02-12", "Hall C", 50, 20.0, "Tech")
    event_id = created["event_id"]
    res = svc.update_event(event_id, {"capacity": 60})
    assert res["success"] is True
