# Project Identification

- **Module**: CO7095 – Software Measurement and Quality Assurance
- **Project Title**: Ticket Booking System
- **Group Members**: srk40, jp697, pcg14, cv92
- **Description**:  
  This project implements a command-line based ticket booking system in Python, supporting user registration, event browsing, ticket booking, and administrative event management. The system emphasizes software quality assurance through extensive testing and code quality metrics.

# Project Overview

The Ticket Booking System enables users to register, log in, search or browse events, book tickets, and manage bookings via a terminal interface. Administrators can create, update, or delete events and generate revenue and occupancy reports.  
**The system does not provide a graphical user interface (GUI) or database backend; all data is persisted using JSON files.**  
The project demonstrates quality assurance practices by integrating black-box/white-box testing, symbolic execution, concolic testing, and code analysis tools.

# Technologies and Tools Used

- **Programming Language**: Python 3.11+
- **IDE**: PyCharm
- **Version Control**: GitHub
- **Testing Tools**:  
  - Pytest (unit and integration testing)
  - Coverage.py (test coverage measurement)
  - Radon (cyclomatic complexity analysis)

# Project Structure

```
ticket_booking/
    cli/                    # CLI interface and controllers
    services/               # Business logic services (auth, bookings, events, pricing, reports)
    storage/                # JSON file storage and repositories
    utils/                  # Validators, exceptions, ID generators, etc.
    data/                   # JSON files for users, events, bookings (persistent storage)
tests/
    srk40/                  # Member: srk40 – owns this test folder
    jp697/                  # Member: jp697 – owns this test folder
    pcg14/                  # Member: pcg14 – owns this test folder
    cv92/                   # Member: cv92 – owns this test folder
README.md
requirements.txt
main.py
```

- **Application code** resides under `ticket_booking/`.
- **Tests** are separated by individual member folders under `tests/`, reflecting responsibility and contributions.

# Installation and Setup

**Requirements**:  
- Python 3.11 or higher (tested on University of Leicester Percy Gee lab machines)
- PyCharm IDE (recommended)

**Setup Steps**:
1. **Clone the repository from GitHub**  
   Open a terminal in PyCharm or the lab computer and run:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

# How to Run the Application

From the project root directory, run:

```bash
python main.py
```

This will launch the command-line interface for user or admin interaction.

# Login Credentials

- **Default Admin Account**:  
  - Username: `admin`
  - Password: `AdminPass123`

- **User Registration**:  
  Any user can register directly from the CLI main menu by choosing the "Register" option and setting their own username and password.

# Features

**User Features:**
- Register for a new account
- Log in and log out
- Browse all available events
- Search events by keyword (name, category, venue)
- Book tickets for selected events (with quantity discounts)
- View all personal bookings
- Cancel active bookings

**Admin Features:**
- Create new events (name, date, venue, capacity, price, category)
- Update existing events
- Delete events (only if there are no active bookings)
- List all events
- Generate revenue reports (total revenue per event)
- Generate occupancy reports (occupancy rates per event)

# Agile Development Process

The project followed **Agile Scrum** methodology:
- Work was divided into multiple sprints, each focusing on specific user stories.
- User stories and sprint progress were tracked using GitHub Projects.
- Regular standups and retrospectives ensured iterative delivery and improvements.

# Testing Strategy

**Black-box Testing:**
- Category partition techniques
- Boundary value analysis
- Random-based input testing

**White-box Testing:**
- Branch and path coverage through code instrumentation

**Symbolic Execution and Concolic Testing:**
- Select modules and functions were analyzed using symbolic execution and concolic tools.
- Execution trees and path conditions are documented within each member’s test folder.

**Ownership:**
- Each group member is responsible for tests in their corresponding subfolder under `tests/`.

# How to Run Tests

- **Run all tests:**
  ```bash
  pytest
  ```

- **Run tests for a specific member:**  
  Replace `srk40` with any member folder as needed.
  ```bash
  pytest srk40/test
  pytest jp697/test
  pytest pcg14/test
  pytest cv92/test
  ```

- **Run tests for a specific technique (e.g., black-box):**
  ```bash
  pytest **/test/blackbox
  pytest **/test/whitebox
  pytest **/test/symbolic
  ```
  (Assumes tests are marked accordingly with pytest markers.)

# Test Coverage Measurement

- **Run tests and measure coverage:**
  ```bash
  coverage run -m pytest
  coverage report
  ```

- **Generate HTML coverage report:**
  ```bash
  coverage html
  open htmlcov/index.html
  # Open htmlcov/index.html in your browser
  ```

# Cyclomatic Complexity Measurement

Radon is used to assess code complexity:

```bash
radon cc ticket_booking/services -a
```

This outputs cyclomatic complexity scores for all modules.

# Symbolic Execution and Concolic Testing

- **Symbolic execution** and **concolic testing** were applied to critical functions, especially in core services.
- Each member’s `tests/<member>/` folder contains:
  - Symbolic execution trees
  - Path condition documentation
- This supports the exploration of possible execution paths for thorough white-box analysis.

# Configuration Management and Contribution

- **Development Workflow:**
  - Each user story is developed on a distinct feature branch.
  - Pull requests are submitted for integration, followed by peer review.
  - Each member’s test contributions reside in their assigned folder.

# Known Limitations

- The system provides a CLI interface only; no GUI is available.
- There is no support for real payment gateways.
- All persistence is handled via local JSON files; no database is used.
- The system is tailored for Python 3.11+ and execution within PyCharm or compatible environments.

# Academic Integrity Statement

This coursework is the original work of srk40, jp697, pcg14, and cv92 for CO7095 at the University of Leicester. All contributions comply with the university’s academic integrity policies. No part of this submission is plagiarized or in violation of assessment regulations.
