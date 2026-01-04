import pytest

# Black-box: Category Partition testing for AuthService
# Focus: register() and login() input categories

@pytest.mark.blackbox
def test_register_valid_user(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.register(username="user1", password="StrongPass123", role="user")
    assert result["success"] is True

@pytest.mark.blackbox
def test_register_duplicate_user(auth_service_fixture):
    svc = auth_service_fixture
    svc.register(username="user1", password="StrongPass123", role="user")
    result = svc.register(username="user1", password="StrongPass123", role="user")
    assert result["success"] is False
    assert "duplicate" in result["message"].lower()

@pytest.mark.blackbox
def test_login_wrong_password(auth_service_fixture):
    svc = auth_service_fixture
    svc.register(username="user2", password="StrongPass123", role="user")
    result = svc.login(username="user2", password="WrongPass999")
    assert result["success"] is False

@pytest.mark.blackbox
def test_login_unknown_user(auth_service_fixture):
    svc = auth_service_fixture
    result = svc.login(username="unknown", password="AnyPass123")
    assert result["success"] is False
