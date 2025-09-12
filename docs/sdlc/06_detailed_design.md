# 6. Detailed Design for NextGenHealth

This document describes the detailed design of the NextGenHealth system, based on the previous phases: [Project Scope](./01_project_scope.md), [Requirements Gathering](./02_requirements_gathering.md), [Feasibility Analysis](./03_feasibility_analysis.md), [Project Planning](./04_project_planning.md), and [System Architecture](./05_system_architecture.md).

The goal is to provide a comprehensive technical specification without including any implementation code, serving as a guide for the development team.

## 6.1 Overview

NextGenHealth is a modular, secure, scalable, and maintainable web system for managing users, appointments, electronic medical records (EMR), reports, and statistics.

The architecture follows **Clean Architecture** and **Domain-Driven Design (DDD)** principles, ensuring:
- Clear separation of concerns
- Technology independence
- Long-term maintainability
- Compliance with healthcare regulations (HIPAA/GDPR)

All modules are designed around **bounded contexts**, with well-defined interfaces and dependencies.

## 6.2 Bounded Contexts and Module Structure

The system is organized into four primary bounded contexts:

| Context | Responsibility |
|--------|----------------|
| **User Management** | Authentication, role-based access, profile management |
| **Appointment Scheduling** | Booking, availability, conflict prevention, notifications |
| **Electronic Medical Records (EMR)** | Clinical data, prescriptions, exam results |
| **Reporting & Analytics** | Statistics, dashboards, exports |

### 6.2.1 User Management Module

#### Responsibilities
- Handle registration and authentication for all user roles:
  - Patient
  - Nurse
  - Doctor
  - Administrator
- Enforce role-based access control (RBAC)
- Manage user profiles and credentials
- Maintain audit trail for all user-related actions

#### Core Entities
- **User**: Base entity with UUID, email, password hash, role, status
- **UserRole**: Enum or mapping table defining permissions per role
- **AuditLogTrail**: Logs all critical actions (login, profile update, etc.)

#### Key Interfaces
- REST API endpoints:
  - `POST /api/v1/auth/register`
  - `POST /api/v1/auth/login`
  - `GET /api/v1/users/me`
  - `PUT /api/v1/users/{uuid}`
- JWT-based authentication with refresh tokens
- Optional 2FA for administrators

#### Business Rules
- Email must be unique across all users
- Passwords must meet complexity requirements (8+ chars, special chars)
- Account locked after 5 failed login attempts
- Audit log entry created for every sensitive action

### 6.2.2 Appointment Scheduling Module

#### Responsibilities
- Allow scheduling and rescheduling of appointments
- Prevent double-booking of doctors
- Prevent overlapping appointments for patients
- Send automated reminders via email/SMS
- Expose availability in real-time

#### Core Entities
- **Appointment**: Links patient, doctor, date/time, type, duration, status
- **DoctorAvailability**: Defines working hours and blocked times
- **TimeSlot**: Value object representing available time windows

#### Key Interfaces
- REST API endpoints:
  - `GET /api/v1/appointments/available-slots?doctor_id=...&date=...`
  - `POST /api/v1/appointments/book`
  - `DELETE /api/v1/appointments/{id}`
- Integration with external services:
  - Email (SendGrid/AWS SES)
  - SMS (Twilio/AWS SNS)

#### Business Rules
- Appointments can be 15, 30, 45, or 60 minutes
- Doctors cannot have overlapping appointments
- Patients cannot book two appointments at the same time
- Cancellations allowed up to 24 hours in advance

### 6.2.3 Electronic Medical Records (EMR) Module

#### Responsibilities
- Allow doctors to create and update medical records
- Link prescriptions and exam results to visits
- Securely store and retrieve medical files
- Track record modifications with versioning

#### Core Entities
- **MedicalRecord**: Contains diagnosis, treatment plan, follow-up notes
- **Prescription**: Digital prescription with medication, dosage, frequency
- **MedicalFile**: Reference to uploaded documents (PDF, images)

#### Key Interfaces
- REST API endpoints:
  - `POST /api/v1/emr/records`
  - `GET /api/v1/emr/records/{patient_id}`
  - `POST /api/v1/emr/files/upload`
- File storage integration (AWS S3)
- Role-based access checks on every request

#### Business Rules
- Only authorized doctors can create/update records
- Prescriptions must be digitally signed
- All record access is logged in audit trail
- Files encrypted at rest

### 6.2.4 Reporting & Analytics Module

#### Responsibilities
- Generate operational reports
- Provide dashboards for administrators
- Support data export for compliance and analysis

#### Key Reports
- Daily/Weekly/Monthly appointment schedules
- No-show and cancellation rates
- New patient registrations by period
- Most common diagnoses
- System usage metrics

#### Key Interfaces
- REST API endpoints:
  - `GET /api/v1/reports/appointments`
  - `GET /api/v1/reports/patients`
  - `GET /api/v1/reports/system`
- Export formats: PDF, Excel
- Admin dashboard with visualizations

#### Business Rules
- Report access restricted by role
- Aggregated data only (no raw PII in analytics)
- Exported files require audit logging

## 6.3 Layered Design

### 6.3.1 Presentation Layer
- **Technologies**: HTML5, CSS3, Bootstrap 5, HTMX
- **Features**:
  - Responsive layout for desktop, tablet, mobile
  - Accessibility compliant (WCAG 2.1 AA)
  - Role-specific views (Patient Portal, Doctor Dashboard, Admin Panel)

### 6.3.2 Application Layer
- **Purpose**: Orchestrate business flows using use cases
- **Components**:
  - Use Case classes (e.g., `RegisterUserUseCase`, `BookAppointmentUseCase`)
  - Request/Response DTOs (Data Transfer Objects)
  - Command/Query separation (CQRS pattern)
  - Cross-cutting services (NotificationService, AuditService)

### 6.3.3 Domain Layer
- **Purpose**: Encapsulate core business logic and rules
- **Components**:
  - Entities (with identity)
  - Value Objects (immutable data)
  - Aggregates (consistency boundaries)
  - Domain Services (logic not belonging to entities)
  - Repositories (interfaces only)
  - Domain Events (e.g., `UserRegisteredEvent`, `AppointmentScheduledEvent`)

### 6.3.4 Infrastructure Layer
- **Purpose**: Implement technical details and integrations
- **Components**:
  - PostgreSQL database with Django ORM
  - Redis for caching and session storage
  - AWS S3 for secure file storage
  - Celery + Redis for background tasks (notifications)
  - External APIs: SendGrid (email), Twilio (SMS)

## 6.4 Data Model (Summary)

| Table | Description |
|------|-------------|
| `users` | Core user data: UUID, email, password_hash, role, status |
| `user_roles` | Mapping between users and roles |
| `patients` | Extended demographic data (linked to `users`) |
| `doctors`, `nurses`, `administrators` | Role-specific profiles |
| `appointments` | Scheduling data: patient, doctor, datetime, status |
| `medical_records` | Clinical documentation and treatment plans |
| `prescriptions` | Medication details linked to records |
| `medical_files` | Metadata and references to stored documents |
| `audit_logs` | Full audit trail for compliance (HIPAA/GDPR) |

> 🔐 All sensitive data encrypted at rest; logs anonymized where appropriate.

## 6.5 Main Workflows

### 6.5.1 User Registration
1. User accesses `/register` form.
2. System validates required fields (email format, password strength).
3. Creates `User` record with hashed password and assigned role.
4. Generates UUID and stores in database.
5. Logs event in `audit_logs`.
6. Sends welcome email via notification service.

### 6.5.2 Appointment Scheduling
1. User selects doctor and date.
2. System retrieves available time slots from `DoctorAvailability`.
3. Validates no conflicts (doctor double-booking, patient overlap).
4. Creates `Appointment` record with status "Scheduled".
5. Sends confirmation to patient (email/SMS).
6. Notifies doctor within 1 hour.
7. Updates calendar views in real-time.

### 6.5.3 Medical Record Creation
1. Doctor opens patient profile.
2. Fills clinical information in EMR form.
3. Submits record linked to appointment.
4. System saves `MedicalRecord` and links to `Prescription` if applicable.
5. Logs access and creation in `audit_logs`.
6. Optionally notifies patient of update.

## 6.6 External Integrations

| Service | Purpose | Integration Method |
|--------|--------|-------------------|
| **SendGrid / AWS SES** | Email notifications | REST API |
| **Twilio / AWS SNS** | SMS reminders | REST API |
| **AWS S3** | Secure file storage | SDK |
| **Sentry** | Error tracking | SDK |
| **New Relic** | Performance monitoring | Agent |

## 6.7 Security and Compliance

- **Authentication**: JWT tokens with refresh mechanism
- **Authorization**: RBAC with policy-based checks
- **Encryption**: TLS 1.3 (in transit), AES-256 (at rest)
- **Auditing**: Structured logs for all sensitive actions
- **Compliance**: HIPAA, GDPR, WCAG 2.1 AA
- **Session Management**: Timeout after 30 minutes of inactivity

## 6.8 Performance Considerations

- **Caching**: Redis for frequent queries (availability, user profiles)
- **Database Indexing**: On `email`, `appointment_datetime`, `patient_id`
- **Pagination**: For large datasets (appointments, records)
- **Asynchronous Processing**: Celery for emails, SMS, report generation
- **Load Testing**: Simulate 1,000 concurrent users

## 6.9 Future Considerations

- **Microservices Migration Path**: Extract bounded contexts into independent services
- **FHIR/HIPAA Interoperability**: Support healthcare data exchange standards
- **Telemedicine Integration**: Video consultation capabilities
- **AI for Predictive Analytics**: Risk scoring, no-show prediction

## 6.10 Conclusion

This detailed design provides a complete blueprint for implementing the NextGenHealth system. It aligns with:
- Clean Architecture
- Domain-Driven Design
- Healthcare compliance requirements
- Scalable and maintainable engineering practices

> **Design Confidence Level: 9/10**

Proceed to the next phase: [Test Plan](./07_test_plan.md)