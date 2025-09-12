# 1. Project Scope Definition

This document defines the scope of the NextGenHealth project, outlining its main objectives, target audience, and key features.

## 1.1 Main Objective

The primary goal of NextGenHealth is to create a secure, scalable healthcare management system that facilitates the efficient management of:
- Users (Patients, Doctors, Nurses, Administrators)
- Appointments
- Medical exams
- Electronic medical records
- Reports and statistics

The system aims to streamline healthcare processes, improve data accessibility, and enhance the overall experience for both healthcare providers and patients, while ensuring compliance with regulations such as HIPAA and LGPD.

## 1.2 Target Audience

NextGenHealth is designed for the following users:

### Clinics
Small to medium-sized healthcare facilities that need a reliable system to manage their operations.

### Hospitals
Larger institutions requiring a scalable solution for patient and appointment management.

### Healthcare Professionals
- **Doctors**: Access patient records, schedule appointments, prescribe treatments.
- **Nurses**: Assist in patient registration, scheduling, and care coordination.
- **Administrators**: Manage user accounts, system settings, and reporting.

### Patients
Individuals who can self-register, book appointments, view available slots, and access their own medical records.

## 1.3 Key Features (High-Level)

The system will include the following core features:

### 1.3.1 User Management

#### User Registration and Roles
- Capture and store user details: name, date of birth, contact info, role (Patient, Doctor, Nurse, Administrator).
- Support **self-registration** (for patients) and **admin-assisted registration** (for staff).
- Assign roles with distinct permissions from the moment of creation.

#### Secure Authentication
- Email-based login with strong password policies.
- Role-based access control (RBAC) enforced across all modules.
- Audit trail of all authentication and profile changes.

#### Profile Management
- Users can update their personal information (patients: self; staff: via admin or designated roles).
- Administrators can manage all user profiles and permissions.

### 1.3.2 Appointment Scheduling

#### Appointment Booking
- Enable scheduling of appointments with:
  - Patient
  - Doctor
  - Date, time, type (consultation, follow-up, examination)
  - Duration (15, 30, 45, 60 minutes)
- Prevent double-booking of doctors and overlapping appointments for patients.
- Support real-time availability checks.

#### Self-Service Booking
- Patients can view available time slots and book their own appointments.
- Nurses and administrators can book on behalf of patients.

#### Appointment Reminders
- Send automated reminders:
  - 48 hours before (email)
  - 24 hours before (SMS)
- Notify doctors of new appointments within 1 hour.

### 1.3.3 Electronic Medical Records (EMR)

#### Record Management
- Doctors can create, update, and access patient medical records.
- Full audit trail of record access and modifications.

#### Exam Results
- Store and display results of medical exams.
- Link exams to specific appointments and diagnoses.

### 1.3.4 Reporting and Statistics

#### Appointment Reports
- Generate reports on completed, canceled, and upcoming appointments by patient, doctor, or date range.

#### Exam Reports
- Provide statistics on requested and completed exams.

#### User Activity Reports
- Track login attempts, appointment bookings, and system actions per user role.

### 1.3.5 Authentication and Access Control

#### Role-Based Access Control (RBAC)
- Define and enforce permissions for each role:
  - **Patient**: View own records, book/cancel appointments, update profile.
  - **Nurse**: View medical records, schedule appointments, update patient information.
  - **Doctor**: Full access to assigned patients’ records, prescriptions, appointments.
  - **Administrator**: Full system access, user management, configuration.

#### Secure Authentication
- Strong password requirements (8+ chars, special chars).
- Account lockout after 5 failed attempts.
- Session timeout after 30 minutes of inactivity.
- Two-Factor Authentication (2FA) for administrators (planned).

#### Audit Trail
- Log all critical actions (logins, bookings, record access) for compliance (HIPAA/LGPD).

## 1.4 Out of Scope

To avoid scope creep, the following features are explicitly out of scope for the initial version of NextGenHealth:
- Integration with external healthcare systems (e.g., government databases).
- Mobile app development (the system will be web-based only).
- Advanced AI-based diagnostics or predictions.
- Billing and insurance processing.

## 1.5 Success Criteria

The project will be considered successful if:
- The system is fully functional and meets the requirements outlined in this document.
- Users (doctors, nurses, administrators, patients) can perform their tasks efficiently using the system.
- The system is deployed and accessible in a production environment.
- All use cases (registration, booking, authentication) are implemented with full auditability and security.

## 1.6 Assumptions and Constraints

### Assumptions:
- Users have basic computer literacy.
- The system will be used in a clinic or hospital with stable internet access.
- Data protection regulations (GDPR, HIPAA) apply and must be followed.

### Constraints:
- The initial version must be completed within 6 months.
- The system must comply with data protection regulations (e.g., GDPR, HIPAA).
- Only email and SMS notifications will be supported initially.

## 1.7 Stakeholders

The main stakeholders for this project are:

- **Project Sponsor**: Provides funding and overall direction.
- **Healthcare Providers**: Doctors, nurses, and administrators who will use the system.
- **Patients**: End-users who will benefit from improved healthcare services.
- **Development Team**: Responsible for designing, developing, and deploying the system.

## 1.8 Next Steps

Finalize and approve this document with stakeholders.  
Proceed to the next phase: [Requirements Gathering](./02_requirements_gathering.md).