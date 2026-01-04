import pytest

# Symbolic Execution (documented + executable checks)

@pytest.mark.symbolic
def test_symbolic_path_valid_login(auth_service_fixture):
    svc = auth_service_fixture
    svc.register(username="sym_user", password="SymPass123", role="user")
    result = svc.login(username="sym_user", password="SymPass123")
    assert result["success"] is True

@pytest.mark.symbolic
def test_symbolic_path_invalid_password(auth_service_fixture):
    svc = auth_service_fixture
    svc.register(username="sym_user2", password="SymPass123", role="user")
    result = svc.login(username="sym_user2", password="bad")
    assert result["success"] is False
