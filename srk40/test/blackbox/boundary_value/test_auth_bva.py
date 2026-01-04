import pytest

# Black-box: Boundary Value Analysis for AuthService

@pytest.mark.blackbox
def test_register_password_min_length(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.register(username="u1", password="Abc12345", role="user")
    assert result["success"] is True

@pytest.mark.blackbox
def test_register_password_below_min_length(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.register(username="u2", password="Abc1234", role="user")
    assert result["success"] is False

@pytest.mark.blackbox
def test_register_username_empty(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.register(username="", password="StrongPass123", role="user")
    assert result["success"] is False
