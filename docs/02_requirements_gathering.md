# 2. Requirements Gathering

This document outlines the functional and non-functional requirements for the **NextGenHealth** system. These requirements are based on the project scope defined in the [Project Scope Definition](./01_project_scope.md).

---

## 2.1 Functional Requirements

Functional requirements describe what the system should do. They are divided into modules based on the key features identified in the project scope.

### 2.1.1 Patient Management
1. **Patient Registration:**
   - The system must allow the registration of new patients with the following information:
     - Full name.
     - Date of birth.
     - Address.
     - Phone number.
     - Email address (used as the primary identifier).
     - National ID (optional, for country-specific identification).
   - The system must generate a unique internal identifier (UUID) for each patient.

2. **Patient Search:**
   - The system must allow healthcare providers to search for patients by:
     - Name.
     - CPF.
     - Date of birth.

### 2.1.2 Appointment Scheduling
1. **Appointment Booking:**
   - The system must allow the scheduling of appointments with the following details:
     - Patient.
     - Doctor.
     - Date and time.
     - Type of appointment (e.g., consultation, exam).
   - The system must prevent double-booking of doctors or patients.

2. **Appointment Reminders:**
   - The system must send reminders to patients via email or SMS 24 hours before the appointment.

### 2.1.3 Electronic Medical Records (EMR)
1. **Record Management:**
   - The system must allow doctors to:
     - Create new medical records.
     - Update existing records.
     - View patient history.
   - Each record must include:
     - Diagnosis.
     - Prescriptions.
     - Exam results.

2. **Exam Results:**
   - The system must allow the upload and display of exam results (e.g., PDFs, images).

### 2.1.4 Reporting and Statistics
1. **Appointment Reports:**
   - The system must generate reports showing:
     - Completed appointments.
     - Canceled appointments.
     - Upcoming appointments.

2. **Exam Reports:**
   - The system must provide statistics on:
     - Requested exams.
     - Completed exams.

### 2.1.5 Authentication and Access Control
1. **User Roles:**
   - The system must define the following roles:
     - Doctor: Can view and update medical records.
     - Nurse: Can view medical records and schedule appointments.
     - Administrator: Can manage users and system settings.

2. **Secure Login:**
   - The system must implement a secure login system with:
     - Password encryption.
     - Session management.

---

## 2.2 Non-Functional Requirements

Non-functional requirements describe how the system should perform and its constraints.

### 2.2.1 Performance
- The system must support up to 1,000 concurrent users without performance degradation.
- Response time for any action must be less than 2 seconds.

### 2.2.2 Security
- The system must comply with data protection regulations (e.g., GDPR, HIPAA).
- All sensitive data must be encrypted both in transit and at rest.

### 2.2.3 Usability
- The system must have an intuitive interface that requires minimal training for users.
- The system must be accessible on both desktop and mobile devices.

### 2.2.4 Scalability
- The system must be designed to handle future growth, such as adding new features or supporting more users.

### 2.2.5 Availability
- The system must have an uptime of 99.9%.
- Regular backups must be performed to prevent data loss.

---

## 2.3 Assumptions and Dependencies

### Assumptions:
- Users have basic computer literacy.
- The system will be used in a clinic or hospital with stable internet access.

### Dependencies:
- The system depends on external services for sending SMS and email reminders.
- The system requires a reliable database for storing patient and appointment data.

---

## 2.4 Next Steps

- Review and validate these requirements with stakeholders.
- Proceed to the next phase: [Feasibility Analysis](./03_feasibility_analysis.md).