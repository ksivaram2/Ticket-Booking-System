import pytest

# White-box: Path coverage for AuthService

@pytest.mark.whitebox
def test_register_weak_password_path(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.register(username="u5", password="123", role="user")
    assert result["success"] is False

@pytest.mark.whitebox
def test_login_wrong_password_path(auth_service_fixture):
    svc = auth_service_fixture
    svc.register(username="u6", password="StrongPass123", role="user")
    result = svc.login(username="u6", password="WrongPass")
    assert result["success"] is False
