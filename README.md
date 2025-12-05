# NextGenHealth

> [!WARNING]
> **Under Construction**  
> This application is currently under development.

> **Next-Generation Healthcare Management System**  
> _Secure, scalable, and role-based — built with Clean Architecture and Python._

NextGenHealth is a healthcare management system designed to streamline patient care, appointment scheduling, medical record access, and administrative workflows for clinics and hospitals. The system follows **Clean Architecture** and **Domain-Driven Design (DDD)** principles to ensure scalability, maintainability, and compliance with regulations such as HIPAA and LGPD.

---

## Key Features

### 1. User Management

- **Role-based user types**: Patient, Nurse, Doctor, Administrator.
- Self-registration for patients; staff registered by administrators.
- Secure profile management and audit trail of changes.
- Centralized identity model with `User` as base entity and role-specific profiles.

### 2. Authentication & Access Control

- Email-based login with strong password policies.
- Role-Based Access Control (RBAC):
  - **Patient**: View own records, book/cancel appointments.
  - **Nurse**: Schedule appointments, view assigned patient records.
  - **Doctor**: Full clinical access to assigned patients.
  - **Administrator**: Full system control, user management, configuration.
- Account lockout after 5 failed attempts.
- Session timeout after 30 minutes of inactivity.
- Audit logging of all authentication and access events.

### 3. Appointment Scheduling

- Real-time availability checks based on doctor schedule.
- Prevention of double-booking and overlapping appointments.
- Self-service booking by patients; nurses and admins can book on behalf of patients.
- Automated reminders:
  - 48 hours before (email)
  - 24 hours before (SMS)
- Cancellation up to 24 hours in advance.

### 4. Electronic Medical Records (EMR)

- Secure creation, update, and access to medical records.
- Full audit trail of record modifications.
- Linking exams and diagnoses to appointments.

### 5. Reporting & Analytics

- Generate reports on:
  - Appointments (by patient, doctor, status)
  - Exam statistics
  - User activity logs

---

## Architecture

The system is structured using **Clean Architecture**, ensuring separation of concerns and testability:

| Layer                 | Responsibility                                                                   |
| --------------------- | -------------------------------------------------------------------------------- |
| **Domain**            | Core business entities and domain rules (`User`, `Appointment`, `MedicalRecord`) |
| **Application**       | Business logic orchestrators (Use Cases) and service interfaces                  |
| **Interface Adapter** | REST API endpoints (Django REST Framework / Flask), controllers                  |
| **Infrastructure**    | Database (PostgreSQL), notification services, audit logging                      |

This design ensures the core business logic remains independent of frameworks and databases.

---

## Tech Stack

| Category             | Technology                                    |
| -------------------- | --------------------------------------------- |
| **Backend**          | Python 3.11+, Django or Flask                 |
| **Database**         | PostgreSQL (production), SQLite (development) |
| **Authentication**   | JWT, OAuth2, Django AllAuth / Flask-Security  |
| **Frontend**         | HTML, CSS, JavaScript, Bootstrap (planned)    |
| **Version Control**  | Git (GitHub)                                  |
| **Testing**          | PyTest, HTTPX, Selenium                       |
| **CI/CD**            | GitHub Actions (planned)                      |
| **Containerization** | Docker (planned)                              |

---

## Installation & Setup

### Prerequisites

- Python 3.11+
- PostgreSQL or SQLite
- Git

### Steps

```bash
# Clone the repository
git clone https://github.com/python-projects-fernando/nextgenhealth.git
cd nextgenhealth

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

---

## Testing

Run unit and integration tests:

```bash
pytest
```

---

## Documentation

Explore the full SDLC process:

- [Project Scope](./docs/sdlc/01_project_scope.md)
- [Requirements Gathering](./docs/sdlc/02_requirements_gathering.md)
- [Feasibility Analysis](./docs/sdlc/03_feasibility_analysis.md)
- [Project Planning](./docs/sdlc/04_project_planning.md)
- [System Architecture](./docs/sdlc/05_system_architecture.md)
- [Detailed Design](./docs/sdlc/06_detailed_design.md)
- [Test Plan](./docs/sdlc/07_test_plan.md)
- [Data Dictionary](./docs/sdlc/08_data_dictionary.md)
- [API Specification](./docs/sdlc/09_api_spec.md)
- [CHANGELOG](CHANGELOG.md)

---

## 👤 Maintained By

This project is developed and maintained by **Fernando Antunes de Magalhães Desenvolvimento de Software Ltda.**

**Fernando Magalhães**  
CEO – FM ByteShift Software  
📞 (21) 97250-1546  
✉️ [contact@fmbyteshiftsoftware.com](mailto:contact@fmbyteshiftsoftware.com)  
🌐 [fmbyteshiftsoftware.com](https://fmbyteshiftsoftware.com)  
🏢 CNPJ: 62.145.022/0001-05 (Brazil)
