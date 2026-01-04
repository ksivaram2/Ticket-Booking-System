import pytest

# Symbolic: verify report paths with / without data (executable checks)

@pytest.mark.symbolic
def test_symbolic_report_empty(report_service_fixture):
    result = report_service_fixture.total_revenue_by_event()
    assert isinstance(result, dict)
