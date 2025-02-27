# 1. Project Scope Definition

This document defines the scope of the **NextGenHealth** project, outlining its main objectives, target audience, and key features.

---

## 1.1 Main Objective

The primary goal of NextGenHealth is to create a **healthcare management system** that facilitates the efficient management of:
- Patients.
- Appointments.
- Medical exams.
- Electronic medical records.
- Reports and statistics.

The system aims to streamline healthcare processes, improve data accessibility, and enhance the overall experience for both healthcare providers and patients.

---

## 1.2 Target Audience

NextGenHealth is designed for the following users:
1. **Clinics:**
   - Small to medium-sized healthcare facilities that need a reliable system to manage their operations.
2. **Hospitals:**
   - Larger institutions requiring a scalable solution for patient and appointment management.
3. **Doctors:**
   - Healthcare professionals who need access to patient records and appointment schedules.
4. **Healthcare Professionals:**
   - Nurses, administrators, and other staff involved in patient care and clinic management.
5. **Patients:**
   - Individuals who need to manage their appointments and view their medical records.

---

## 1.3 Key Features (High-Level)

The system will include the following core features:

### 1.3.1 Patient Management
- **Patient Registration:**
  - Capture and store patient details such as name, date of birth, address, phone number, email, and national ID.
  - Patients can register themselves or be registered by an administrator.
- **Patient Search:**
  - Allow healthcare providers to search for patients by name, national ID, or other identifiers.

### 1.3.2 Appointment Scheduling
- **Appointment Booking:**
  - Enable the scheduling of appointments, associating patients, doctors, date, and time.
  - Patients can view available time slots and book their own appointments.
- **Appointment Reminders:**
  - Send reminders to patients via email or SMS.
  - Patients can also view their upcoming appointments in the system.

### 1.3.3 Electronic Medical Records (EMR)
- **Record Management:**
  - Allow doctors to create, update, and access patient medical records.
- **Exam Results:**
  - Store and display results of medical exams.

### 1.3.4 Reporting and Statistics
- **Appointment Reports:**
  - Generate reports of completed, canceled, and upcoming appointments.
- **Exam Reports:**
  - Provide statistics on requested and completed exams.

### 1.3.5 Authentication and Access Control
- **User Roles:**
  - Define roles such as doctor, nurse, administrator, and patient with different access levels.
  - Patients can register themselves, manage their appointments, and view their own medical records.
- **Secure Login:**
  - Implement a secure authentication system to protect sensitive data.

---

## 1.4 Out of Scope

To avoid scope creep, the following features are explicitly **out of scope** for the initial version of NextGenHealth:
- Integration with external healthcare systems (e.g., government databases).
- Mobile app development (the system will be web-based only).
- Advanced AI-based diagnostics or predictions.

---

## 1.5 Success Criteria

The project will be considered successful if:
1. The system is fully functional and meets the requirements outlined in this document.
2. Users (doctors, nurses, administrators, patients) can perform their tasks efficiently using the system.
3. The system is deployed and accessible in a production environment.

---

## 1.6 Assumptions and Constraints

### Assumptions:
- Users have basic computer literacy.
- The system will be used in a clinic or hospital with stable internet access.

### Constraints:
- The initial version must be completed within 6 months.
- The system must comply with data protection regulations (e.g., GDPR, HIPAA).

---

## 1.7 Stakeholders

The main stakeholders for this project are:
1. **Project Sponsor:**
   - Provides funding and overall direction.
2. **Healthcare Providers:**
   - Doctors, nurses, and administrators who will use the system.
3. **Patients:**
   - End-users who will benefit from improved healthcare services.
4. **Development Team:**
   - Responsible for designing, developing, and deploying the system.

---

## 1.8 Next Steps

- Finalize and approve this document with stakeholders.
- Proceed to the next phase: [Requirements Gathering](./02_requirements_gathering.md).