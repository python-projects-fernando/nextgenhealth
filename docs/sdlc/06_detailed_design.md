# 6. Detailed Design for NextGenHealth

This document describes the **detailed design** of the **NextGenHealth** system, based on the previous phases: [Project Scope](./01_project_scope.md), [Requirements Gathering](./02_requirements_gathering.md), [Feasibility Analysis](./03_feasibility_analysis.md), [Project Planning](./04_project_planning.md), and [System Architecture](./05_system_architecture.md).

The goal is to provide a **comprehensive technical specification** without including any implementation code, serving as a guide for the development team.

---

## 6.1 Overview

NextGenHealth will be a modular, secure, scalable, and maintainable **web system** for managing patients, appointments, electronic medical records (EMR), reports, and statistics.  
The architecture follows **Clean Architecture** and **Domain-Driven Design (DDD)** principles, ensuring separation of concerns and technology independence.

---

## 6.2 Module Structure

### 6.2.1 User Management Module
- **Responsibilities**:
  - User authentication and authorization.
  - Role-based access control (RBAC).
  - Registration and management of patient and healthcare professional accounts.
- **Key Entities**:
  - `User`
  - `UserRole`
  - `AuditLog`
- **Interfaces**:
  - REST API for login, registration, and profile management.
  - Two-factor authentication integration for administrators.

### 6.2.2 Patient Management Module
- **Responsibilities**:
  - Register and update patient data.
  - Search patients by multiple criteria.
  - Maintain change history.
- **Key Entities**:
  - `Patient`
  - `PersonalInfo`
  - `ContactInfo`
  - `Address`
- **Interfaces**:
  - API for patient CRUD operations.
  - Advanced search and filtering.

### 6.2.3 Appointment Management Module
- **Responsibilities**:
  - Create, update, and cancel appointments.
  - Prevent scheduling conflicts.
  - Send automatic notifications to patients and doctors.
- **Key Entities**:
  - `Appointment`
  - `Doctor`
  - `DoctorAvailability`
- **Interfaces**:
  - Scheduling and availability API.
  - Integration with email/SMS for reminders.

### 6.2.4 Electronic Medical Records (EMR) Module
- **Responsibilities**:
  - Record and update clinical information.
  - Manage prescriptions and exam results.
- **Key Entities**:
  - `MedicalRecord`
  - `Prescription`
  - `MedicalFile`
- **Interfaces**:
  - API for EMR CRUD operations.
  - Secure document upload (PDF, medical images).

### 6.2.5 Reporting and Statistics Module
- **Responsibilities**:
  - Generate appointment, patient, and system usage reports.
  - Export data in PDF and Excel formats.
- **Key Entities**:
  - Reports (non-persistent, generated on demand).
- **Interfaces**:
  - API for report generation with filters.
  - Admin dashboard with visualizations.

---

## 6.3 Layered Design

### 6.3.1 Presentation Layer
- **Technologies**: HTML5, CSS3, Bootstrap 5, HTMX.
- **Features**:
  - Responsive layout.
  - Accessibility (WCAG 2.1 AA).
  - Dedicated pages for patients, doctors, and administrators.

### 6.3.2 Application Layer
- **Purpose**: Orchestrates use cases.
- **Components**:
  - Application services.
  - DTOs for input/output data.
  - Command/Query separation (CQRS).

### 6.3.3 Domain Layer
- **Purpose**: Contains core business rules and entities.
- **Components**:
  - Entities, value objects, aggregates.
  - Domain services.
  - Domain events for internal communication.

### 6.3.4 Infrastructure Layer
- **Purpose**: Handles technical implementations.
- **Components**:
  - Data persistence (PostgreSQL).
  - Caching (Redis).
  - File storage (AWS S3).
  - Integration with external services (SendGrid, Twilio).

---

## 6.4 Data Model (Summary)

| Entity            | Description |
|-------------------|-------------|
| **users**         | Authentication and role data. |
| **patients**      | Personal and contact details. |
| **doctors**       | Professional information and availability. |
| **appointments**  | Scheduling with status and time slots. |
| **medical_records** | Full electronic medical records. |
| **prescriptions** | Medical prescriptions linked to records. |
| **medical_files** | References to medical documents/exams. |
| **audit_logs**    | Activity logs for compliance. |

---

## 6.5 Main Workflows

### 6.5.1 Patient Registration
1. User accesses registration form.
2. System validates required fields.
3. Generates a UUID for the patient.
4. Stores the record in the database.
5. Records the event in the audit log.

### 6.5.2 Appointment Scheduling
1. Patient or healthcare provider selects date and doctor.
2. System checks availability.
3. Creates appointment record.
4. Sends confirmation notifications.

### 6.5.3 Medical Record Creation
1. Doctor opens the patient profile.
2. Fills in clinical information.
3. System saves the record and generates a version.
4. Notifies the patient of the update.

---

## 6.6 External Integrations

- **Email Service (SendGrid/AWS SES)**: Send notifications and reports.
- **SMS Service (Twilio/AWS SNS)**: Appointment reminders.
- **Cloud Storage (AWS S3)**: Medical file storage.
- **REST APIs**: Future integrations with external systems (labs, pharmacies).

---

## 6.7 Security and Compliance

- **Authentication**: JWT + 2FA for administrators.
- **Authorization**: Strict RBAC.
- **Encryption**: TLS 1.3 (in transit), AES-256 (at rest).
- **Auditing**: Detailed logging of access and changes.
- **Compliance**: HIPAA, GDPR, and local regulations.

---

## 6.8 Performance Considerations

- Cache critical data with Redis.
- Database indexing for frequent queries.
- Pagination for large datasets.
- Asynchronous processing (Celery) for notifications and heavy reports.

---

## 6.9 Future Considerations

- Support for DICOM medical image format.
- Multi-clinic deployment with data isolation.
- Partial migration to microservices as the system grows.

---

Proceed to the next phase: [Test Plan](07_test_plan.md)
