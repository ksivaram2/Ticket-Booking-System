import pytest

# White-box: Branch coverage tests for AuthService

@pytest.mark.whitebox
def test_register_invalid_role_branch(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.register(username="u3", password="StrongPass123", role="invalid_role")
    assert result["success"] is False

@pytest.mark.whitebox
def test_login_success_branch(auth_service_fixture):
    svc = auth_service_fixture
    svc.register(username="u4", password="StrongPass123", role="user")
    result = svc.login(username="u4", password="StrongPass123")
    assert result["success"] is True
