import pytest

# Concolic testing template: concrete inputs derived from constraints

@pytest.mark.concolic
def test_concolic_unknown_user(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.login(username="no_such_user", password="AnyPass123")
    assert result["success"] is False

@pytest.mark.concolic
def test_concolic_success(auth_service_fixture):
    svc = auth_service_fixture
    svc.register(username="c_user", password="Cpass12345", role="user")
    result = svc.login(username="c_user", password="Cpass12345")
    assert result["success"] is True
