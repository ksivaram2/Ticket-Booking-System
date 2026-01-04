Concolic Constraints for BookingService.book

Path A (not found):
- event_exists(event_id) = False

Path B1 (invalid quantity):
- event_exists(event_id) = True
- q <= 0

Path C1 (insufficient capacity):
- event_exists(event_id) = True
- q > 0
- capacity < q

Path C2 (success):
- event_exists(event_id) = True
- q > 0
- capacity >= q
