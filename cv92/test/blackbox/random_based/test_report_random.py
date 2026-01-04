import pytest

# Black-box: Random based smoke checks for report functions

@pytest.mark.blackbox
def test_report_smoke(report_service_fixture):
    assert isinstance(report_service_fixture.total_revenue_by_event(), dict)
    assert isinstance(report_service_fixture.occupancy_rates(), dict)
