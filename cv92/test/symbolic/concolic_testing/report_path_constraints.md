Concolic Constraints for ReportService.total_revenue_by_event

Path A (empty):
- bookings = []

Path B2 (active booking contributes):
- bookings contains at least one item with status="active"
- total_price is numeric
