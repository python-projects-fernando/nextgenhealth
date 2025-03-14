# Use Case Specification: **View**

## 1. Overview

This document specifies the **"View"** use case for the **NextGenHealth** system. The purpose of this use case is to allow **Users (Patients, Administrators, Doctors, Nurses)** to view relevant data in the system based on their role and permissions. This includes viewing their own profile (in the case of the user/patient) or viewing other records as needed (in the case of administrators, doctors, and nurses).

---

## 2. Use Case Details

### 2.1 Use Case ID  
**UC-07**: View

### 2.2 Actors
- **Primary Actor**: User/Patient, Administrator, Doctor, Nurse
- **Secondary Actor**: System (displays the requested data)

### 2.3 Preconditions
- The user must be authenticated.
- The user must have the appropriate permissions to view the data.
  - A **patient** can only view their own profile and records.
  - **Administrators**, **Doctors**, and **Nurses** can view the patient profiles, appointments, and exam records.

### 2.4 Postconditions
- The requested data is displayed to the user.
- The user can view detailed information, such as personal details, medical history, appointments, exams, etc.

### 2.5 Trigger
- The user navigates to their profile page (for patients) or selects a patient record (for administrators, doctors, and nurses).

---

## 3. Basic Flow (Main Success Scenario)

### **User Viewing Their Own Profile (for Patient):**
1. The patient logs into the system.
2. The patient navigates to their profile page.
3. The system displays the patient's personal information, medical history, appointments, and exam results.
4. The patient can view the information but cannot modify it.

### **Administrator, Doctor, or Nurse Viewing a Patient’s Profile:**
1. The administrator, doctor, or nurse logs into the system.
2. The user searches for a specific patient or selects a patient from a list (depending on their permissions).
3. The system displays the patient's profile, including personal information, medical history, appointments, and exam results.
4. The user can view the information but cannot modify it unless they have permissions for that (e.g., editing or updating patient records).

---

### Alternative Flow:
- If the user (patient, administrator, doctor, or nurse) cannot find the patient’s profile due to incorrect search criteria, the system will display a message indicating no results were found.
- If the user does not have the necessary permissions to view certain information, the system will display a "permission denied" message or restrict access to those specific sections.

---

## 4. Special Requirements

- **Role-Based Access Control (RBAC):** 
  - Patients can only view their own records.
  - Administrators, doctors, and nurses can view patient profiles, medical history, appointments, and exam results.
- **Data Security and Privacy:** Sensitive information should be displayed securely, ensuring compliance with data protection regulations (e.g., HIPAA).
- **Audit Logging:** Viewing actions should be logged for security purposes, especially for administrators, doctors, and nurses.

---

## 5. Exceptions

- If the system is down or cannot access the database, the system will display an error message.
- If the user attempts to access a record they are not authorized to view, the system will restrict access and inform them with a "permission denied" message.
- If the user does not find the expected data due to incorrect search criteria, the system will display a message indicating that no records were found.

---

## 6. Relationships

- **Include:**  
  - **Audit Log**: Viewing actions should be logged for security purposes, especially for administrators, doctors, and nurses.

---

## 7. Assumptions

- The user has the appropriate permissions to view the requested information.
- The system ensures all sensitive patient data is displayed securely and in compliance with applicable laws.

---

## 8. Notes

- The system should display a user-friendly interface for both patients and medical staff to easily navigate and view records.
- To avoid overwhelming users, the system may paginate large sets of data (e.g., medical history) into manageable sections.
- Patients should be notified if critical information (e.g., contact details or health records) is updated or viewed by authorized personnel.

