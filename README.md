# NextGenHealth

## Overview
**NextGenHealth** is a healthcare management system designed to facilitate patient management, appointment scheduling, medical record-keeping, and report generation for clinics and hospitals. The system follows **Clean Architecture** principles with elements of **Domain-Driven Design (DDD)** to ensure scalability and maintainability.

## Features
- **User Authentication & Access Control** (Admin, Doctor, Nurse, etc.).
- **Patient Management** (Registration, Profile Updates, Medical Records).
- **Appointment Scheduling** (Conflict Detection, Calendar View).
- **Medical Records Handling** (Secure Storage, Role-Based Access).
- **Reports & Analytics** (Patient History, Hospital Statistics).
- **Notifications & Reminders** (Email/SMS Alerts).

## Architecture
The system is structured using **Clean Architecture**, which separates concerns into distinct layers:

1. **Domain Layer** – Core business logic, entities (`Patient`, `Doctor`, `Appointment`).
2. **Application Layer** – Use cases and services (`ScheduleAppointmentService`).
3. **Interface Layer** – REST API endpoints (Django REST Framework / Flask).
4. **Infrastructure Layer** – Database, authentication, external services (PostgreSQL, MySQL, SQLite).

## Tech Stack
- **Backend:** Python, Django/Flask, PostgreSQL/MySQL.
- **Frontend:** HTML, CSS, JavaScript (Bootstrap or React).
- **Version Control:** Git (GitHub/Azure DevOps).
- **Testing:** PyTest, Selenium, Postman.

## Installation & Setup
### Prerequisites
- Python 3.8+
- PostgreSQL/MySQL (or SQLite for development)
- Git

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/nextgenhealth.git
   cd nextgenhealth
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```sh
   python manage.py migrate
   ```
5. Run the application:
   ```sh
   python manage.py runserver
   ```

## Testing
Run unit tests with:
```sh
pytest
```

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to your branch: `git push origin feature-branch`.
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

For more details, check the **[Initial Documentation](./docs/06_initial_documentation.md)**.

