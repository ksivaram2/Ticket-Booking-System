import pytest

# Concolic: concrete values derived from path constraints

@pytest.mark.concolic
def test_concolic_update_not_found(event_service_fixture):
    svc = event_service_fixture
    res = svc.update_event("E000", {"capacity": 10})
    assert res["success"] is False
