from ticket_booking.cli.prompts import prompt_choice, prompt_text
from ticket_booking.cli.cli_controller import CLIController


def run_cli() -> None:
    ctl = CLIController()

    while True:
        if not ctl.is_logged_in():
            _public_menu(ctl)
        else:
            role = ctl.current_user.get("role", "user")
            if role == "admin":
                _admin_menu(ctl)
            else:
                _user_menu(ctl)


def _public_menu(ctl: CLIController) -> None:
    choice = prompt_choice("Ticket Booking System", ["Register", "Login", "Exit"])

    if choice == 1:
        username = prompt_text("Username")
        password = prompt_text("Password")
        res = ctl.register(username, password)
        print(res.get("message", ""))

    elif choice == 2:
        username = prompt_text("Username")
        password = prompt_text("Password")
        res = ctl.login(username, password)
        print(res.get("message", ""))

    else:
        print("Goodbye.")
        raise SystemExit(0)


def _user_menu(ctl: CLIController) -> None:
    username = ctl.current_user["username"]

    choice = prompt_choice(
        f"User Menu (logged in as: {username})",
        [
            "Browse Events",
            "Search Events",
            "Book Tickets",
            "My Bookings",
            "Cancel Booking",
            "Logout",
        ],
    )

    if choice == 1:
        events = ctl.events.list_events()
        _print_events(events)

    elif choice == 2:
        keyword = prompt_text("Enter keyword (name/category/venue)")
        matches = ctl.events.search_events(keyword)
        _print_events(matches)

    elif choice == 3:
        event_id = prompt_text("Event ID")
        qty_raw = prompt_text("Quantity")
        try:
            qty = int(qty_raw)
        except ValueError:
            print("Quantity must be an integer.")
            return

        res = ctl.bookings.book(event_id=event_id, username=username, quantity=qty)
        print(res.get("message", ""))
        if res.get("success"):
            print(f"Booking ID: {res.get('booking_id')}, Total Price: {res.get('total_price')}")

    elif choice == 4:
        bookings = ctl.bookings.list_by_user(username)
        _print_bookings(bookings)

    elif choice == 5:
        booking_id = prompt_text("Booking ID")
        res = ctl.bookings.cancel(booking_id)
        print(res.get("message", ""))

    else:
        ctl.logout()
        print("Logged out.")


def _admin_menu(ctl: CLIController) -> None:
    username = ctl.current_user["username"]

    choice = prompt_choice(
        f"Admin Menu (logged in as: {username})",
        [
            "Create Event",
            "Update Event",
            "Delete Event",
            "Browse Events",
            "Revenue Report",
            "Occupancy Report",
            "Logout",
        ],
    )

    if choice == 1:
        name = prompt_text("Name")
        date = prompt_text("Date (YYYY-MM-DD)")
        venue = prompt_text("Venue")
        capacity_raw = prompt_text("Capacity")
        price_raw = prompt_text("Base Price")
        category = prompt_text("Category")

        try:
            capacity = int(capacity_raw)
            base_price = float(price_raw)
        except ValueError:
            print("Capacity must be int, Base Price must be number.")
            return

        res = ctl.events.create_event(name, date, venue, capacity, base_price, category)
        print(res.get("message", ""))
        if res.get("success"):
            print(f"Event ID: {res.get('event_id')}")

    elif choice == 2:
        event_id = prompt_text("Event ID")
        field = prompt_text("Field to update (name/date/venue/capacity/base_price/category)")
        value = prompt_text("New value")

        updates = {field: value}
        res = ctl.events.update_event(event_id, updates)
        print(res.get("message", ""))

    elif choice == 3:
        event_id = prompt_text("Event ID")
        res = ctl.events.delete_event(event_id)
        print(res.get("message", ""))

    elif choice == 4:
        events = ctl.events.list_events()
        _print_events(events)

    elif choice == 5:
        report = ctl.reports.total_revenue_by_event()
        if not report:
            print("No revenue data.")
        else:
            print("Revenue by Event:")
            for eid, amt in report.items():
                print(f"- {eid}: {amt}")

    elif choice == 6:
        report = ctl.reports.occupancy_rates()
        if not report:
            print("No occupancy data.")
        else:
            print("Occupancy Rates:")
            for eid, rate in report.items():
                print(f"- {eid}: {rate}")

    else:
        ctl.logout()
        print("Logged out.")


def _print_events(events: list[dict]) -> None:
    if not events:
        print("No events found.")
        return
    print("\nEvents:")
    for e in events:
        print(
            f"- {e.get('event_id')} | {e.get('name')} | {e.get('date')} | {e.get('venue')} "
            f"| cap={e.get('capacity')} | price={e.get('base_price')} | {e.get('category')}"
        )


def _print_bookings(bookings: list[dict]) -> None:
    if not bookings:
        print("No bookings found.")
        return
    print("\nBookings:")
    for b in bookings:
        print(
            f"- {b.get('booking_id')} | event={b.get('event_id')} | qty={b.get('quantity')} "
            f"| total={b.get('total_price')} | status={b.get('status')}"
        )
