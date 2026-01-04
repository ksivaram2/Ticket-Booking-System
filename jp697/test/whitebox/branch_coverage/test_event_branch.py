import pytest

# White-box: Branch coverage for EventService

@pytest.mark.whitebox
def test_update_event_not_found_branch(event_service_fixture):
    svc = event_service_fixture
    result = svc.update_event(event_id="E999", updates={"capacity": 200})
    assert result["success"] is False

@pytest.mark.whitebox
def test_delete_event_not_found_branch(event_service_fixture):
    svc = event_service_fixture
    result = svc.delete_event("E404")
    assert result["success"] is False
