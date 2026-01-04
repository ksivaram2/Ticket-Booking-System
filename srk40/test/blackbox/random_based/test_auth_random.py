import pytest
import random
import string

# Black-box: Random Based Testing for AuthService

def _rand_str(n: int) -> str:
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(n))

@pytest.mark.blackbox
def test_register_random_inputs(auth_service_fixture):
    svc = auth_service_fixture
    for _ in range(20):
        username = _rand_str(random.randint(1, 20))
        password = _rand_str(random.randint(1, 20))
        result = svc.register(username=username, password=password, role="user")
        assert "success" in result
