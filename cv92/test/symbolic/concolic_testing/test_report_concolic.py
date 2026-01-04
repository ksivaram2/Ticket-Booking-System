import pytest

# Concolic: concrete tests derived from constraints (empty data path)

@pytest.mark.concolic
def test_concolic_empty_data(report_service_fixture):
    res = report_service_fixture.total_revenue_by_event()
    assert res == {}
