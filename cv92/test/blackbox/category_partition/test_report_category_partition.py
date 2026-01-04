import pytest

# Black-box: Report generation validity

@pytest.mark.blackbox
def test_report_revenue_empty(report_service_fixture):
    result = report_service_fixture.total_revenue_by_event()
    assert isinstance(result, dict)
