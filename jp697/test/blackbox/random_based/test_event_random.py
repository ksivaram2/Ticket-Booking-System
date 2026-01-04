import pytest
import random
import string

# Black-box: Random based testing for EventService

def _rand(n: int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(n))

@pytest.mark.blackbox
def test_random_event_names(event_service_fixture):
    svc = event_service_fixture
    for _ in range(10):
        name = _rand(8)
        res = svc.create_event(name, "2026-02-12", "Venue", 10, 12.5, "Cat")
        assert "success" in res
