Concolic Constraints for EventService.update_event

Path A (not found):
- event_exists(event_id) = False
Example: event_id="E000", updates={"capacity":10}

Path C1 (invalid capacity):
- event_exists(event_id) = True
- capacity_update_present = True
- capacity <= 0
Example: capacity=-5

Path C2 (valid capacity):
- event_exists(event_id) = True
- capacity_update_present = True
- capacity > 0
Example: capacity=60
