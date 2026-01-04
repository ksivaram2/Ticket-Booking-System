import pytest

# Black-box: Boundary tests for reports (empty vs non-empty)

@pytest.mark.blackbox
def test_occupancy_empty(report_service_fixture):
    result = report_service_fixture.occupancy_rates()
    assert isinstance(result, dict)
