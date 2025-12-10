# Ticket Booking System

A command-line interface (CLI) application for managing event ticket bookings with user authentication, event management, and comprehensive reporting capabilities.

## Project Structure

```
ticket_booking/
├── __init__.py
├── main.py                     # CLI entry point
├── models/                     # Data models
│   ├── __init__.py
│   ├── user.py                # User class definition
│   ├── event.py               # Event class definition
│   └── booking.py             # Booking class definition
├── services/                   # Business logic layer
│   ├── __init__.py
│   ├── auth_service.py        # Authentication (login/register)
│   ├── event_service.py       # Event CRUD operations and search
│   ├── booking_service.py     # Booking, cancellation, pricing logic
│   └── report_service.py      # Admin reports and statistics
├── storage/                    # Data persistence layer
│   ├── __init__.py
│   └── file_storage.py        # JSON/text file operations
├── utils/                      # Helper utilities
│   ├── __init__.py
│   ├── validators.py          # Input and business rule validation
│   └── id_generator.py        # Unique ID generation
└── [srk40,jp697,pcg14,cv92]/          # Individual test directories
    └── test/
        ├── blackbox/          # Black box testing
        ├── whitebox/          # White box testing
        └── symbolic/          # Symbolic execution testing
```

## Features

### Core Functionality
- **User Management**: User registration and authentication
- **Event Management**: Create, read, update, and delete events
- **Booking System**: Book tickets, cancel bookings, and manage reservations
- **Pricing Engine**: Dynamic pricing calculation based on event attributes
- **Search Capabilities**: Find events by various criteria
- **Admin Reports**: Generate statistics and analytics

### User Roles
- **Regular Users**: Browse events, book tickets, manage their bookings
- **Administrators**: Full access to event management and reporting features

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ticket_booking
```

2. Ensure Python 3.7+ is installed:
```bash
python --version
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Usage

Run the application from the command line:

```bash
python main.py
```

Follow the interactive CLI prompts to:
- Register or log in
- Browse available events
- Book tickets
- View your bookings
- Cancel bookings (if applicable)
- Access admin features (for authorized users)

## Development

### Architecture Overview

The application follows a layered architecture pattern:

1. **Presentation Layer** (`main.py`): Handles user interaction via CLI
2. **Service Layer** (`services/`): Contains business logic and orchestration
3. **Model Layer** (`models/`): Defines data structures and entities
4. **Storage Layer** (`storage/`): Manages data persistence
5. **Utility Layer** (`utils/`): Provides helper functions and validation

### Key Components

#### Models
- **User**: Represents system users with authentication credentials
- **Event**: Defines event details (name, date, venue, capacity, pricing)
- **Booking**: Links users to events with booking status and metadata

#### Services
- **AuthService**: Handles user authentication and authorization
- **EventService**: Manages event lifecycle and search functionality
- **BookingService**: Processes ticket bookings and cancellations
- **ReportService**: Generates analytics for administrators

#### Storage
- **FileStorage**: Implements data persistence using JSON or text files

#### Utils
- **Validators**: Ensures data integrity and business rule compliance
- **IDGenerator**: Creates unique identifiers for entities

## Testing

The project includes comprehensive testing organized by team members:

### Test Categories
- **Black Box Testing**: Functional testing without knowledge of internal implementation
- **White Box Testing**: Structural testing with full code visibility
- **Symbolic Testing**: Automated test generation using symbolic execution

### Running Tests

Navigate to individual team member directories to run their test suites:

```bash
cd srk40/test/blackbox
python -m pytest
```

## Data Storage

Data is persisted in JSON format in the `storage/` directory. The following files are managed:
- `users.json`: User account information
- `events.json`: Event catalog
- `bookings.json`: Booking records

## Contributing

### Team Members
- **srk40**: [Role/Responsibilities]
- **jp697**: [Role/Responsibilities]
- **pcg14**: [Role/Responsibilities]
- **cv92**: [Role/Responsibilities]

### Development Workflow
1. Create a feature branch from `main`
2. Implement changes following the established architecture
3. Write appropriate tests in your team member directory
4. Submit a pull request for code review
5. Merge after approval and passing tests

## Future Enhancements

- [ ] Database integration (PostgreSQL/MySQL)
- [ ] REST API for web/mobile clients
- [ ] Payment gateway integration
- [ ] Email notifications
- [ ] Seat selection interface
- [ ] Multi-language support
- [ ] Advanced analytics dashboard

## License

[Specify your license here]

## Contact

For questions or support, please contact the development team.

---

**Version**: 1.0.0  
**Last Updated**: 2025
