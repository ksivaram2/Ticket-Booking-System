Symbolic Execution Tree (ReportService.total_revenue_by_event)

Inputs:
- bookings list (symbolic sequence)

Node 1: bookings_empty?
  Path A: True  -> return {}
  Path B: False -> Node 2

Node 2: for each booking: status == "active"?
  Path B1: False -> ignore booking
  Path B2: True  -> add total_price to event revenue
