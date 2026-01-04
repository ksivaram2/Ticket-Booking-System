Symbolic Execution Tree (BookingService.book)

Inputs:
- event_id (symbolic)
- quantity q (symbolic integer)

Node 1: event_exists(event_id)?
  Path A: False -> failure ("Event not found")
  Path B: True  -> Node 2

Node 2: q > 0 ?
  Path B1: False -> failure ("Quantity must be positive")
  Path B2: True  -> Node 3

Node 3: capacity >= q ?
  Path C1: False -> failure ("Insufficient capacity")
  Path C2: True  -> success (booking created)
