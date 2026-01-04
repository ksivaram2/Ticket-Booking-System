import pytest

# White-box: Branch coverage on report functions (no events vs events)

@pytest.mark.whitebox
def test_report_handles_no_events_branch(report_service_fixture):
    result = report_service_fixture.occupancy_rates()
    assert isinstance(result, dict)
