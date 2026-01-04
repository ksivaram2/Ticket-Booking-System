import pytest

# Symbolic execution checks for update_event paths

@pytest.mark.symbolic
def test_symbolic_update_capacity_valid(event_service_fixture):
    svc = event_service_fixture
    created = svc.create_event("Expo", "2026-02-12", "Hall B", 50, 20.0, "Tech")
    event_id = created["event_id"]
    result = svc.update_event(event_id=event_id, updates={"capacity": 60})
    assert result["success"] is True
