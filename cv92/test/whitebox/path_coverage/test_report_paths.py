import pytest

# White-box: Path coverage for reports (with and without booking data)

@pytest.mark.whitebox
def test_revenue_path_empty(report_service_fixture):
    res = report_service_fixture.total_revenue_by_event()
    assert res == {}
