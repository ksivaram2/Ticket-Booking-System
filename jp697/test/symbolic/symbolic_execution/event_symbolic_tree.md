Symbolic Execution Tree (EventService.update_event)

Inputs:
- event_id (symbolic)
- updates.capacity (symbolic integer)

Node 1: event_exists(event_id)?
  Path A: False -> failure ("Event not found")
  Path B: True  -> Node 2

Node 2: capacity_update_present?
  Path B1: False -> success (no capacity change)
  Path B2: True  -> Node 3

Node 3: capacity > 0 ?
  Path C1: False -> failure ("Capacity must be positive")
  Path C2: True  -> success (event updated)
