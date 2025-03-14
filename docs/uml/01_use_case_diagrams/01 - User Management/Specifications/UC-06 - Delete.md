# Use Case Specification: **Delete**

## 1. Overview

This document specifies the **"Delete"** use case for the **NextGenHealth** system. The purpose of this use case is to allow the **Administrator** to delete patient records, appointments, or exams as necessary, ensuring proper access control and auditing.

---

## 2. Use Case Details

### 2.1 Use Case ID  
**UC-06**: Delete

### 2.2 Actors
- **Primary Actor**: Administrator
- **Secondary Actor**: System (performs the deletion)

### 2.3 Preconditions
- The user must be authenticated as an administrator.
- The administrator has the necessary permissions to delete records.
- The system must ensure that the deletion is valid and that no critical records are accidentally deleted.

### 2.4 Postconditions
- The deleted record is permanently removed from the system.
- A confirmation message is displayed to the administrator confirming the deletion.
- An audit log is generated to record the deletion event for compliance and tracking purposes.

### 2.5 Trigger
- The administrator initiates a delete action from the system, either from the patient’s profile, appointment page, or exam record.

---

## 3. Basic Flow (Main Success Scenario)

### **Administrator Deleting a Record:**
1. The administrator navigates to the record (patient, appointment, or exam) that needs to be deleted.
2. The administrator clicks the "Delete" button or option.
3. The system prompts the administrator with a confirmation message to prevent accidental deletion.
4. The administrator confirms the deletion.
5. The system permanently deletes the record from the database.
6. The system displays a success message confirming the deletion.
7. An audit log is generated documenting the deletion action.

---

### Alternative Flow:
- If the administrator decides not to delete the record after the confirmation prompt, the system cancels the deletion and returns to the previous page.
- If the administrator lacks permission to delete the record, the system will inform the administrator that the action is prohibited.

---

## 4. Special Requirements

- **Access Control:** Only the administrator can delete records. No other roles (e.g., nurse, doctor, or patient) have permission to delete records.
- **Audit Logging:** All deletion actions must be logged for security, auditing, and compliance purposes.
- **Confirmation Prompt:** The system should display a confirmation message to the administrator before performing any deletion to avoid accidental loss of data.
- **Data Integrity:** Deletion of patient records, appointments, or exams should ensure that no related data (such as medical history) is compromised unless necessary.

---

## 5. Exceptions

- If the system is down or cannot access the database, the system will display an error message.
- If the administrator tries to delete a record that is required for legal, compliance, or medical reasons, the system will prevent the deletion and inform the administrator.
- If the administrator does not have sufficient permissions to delete the record, the system will inform the administrator that the action is prohibited.

---

## 6. Relationships

- **Include:**  
  - **Audit Log**: Every delete action must include logging the event for audit purposes.

---

## 7. Assumptions

- The administrator has the appropriate permissions to perform the delete action.
- The system will handle related data integrity when a record is deleted (e.g., if deleting a patient record, related appointments or exams should also be considered for removal if applicable).

---

## 8. Notes

- The system should ensure that critical records, such as those related to ongoing treatments, cannot be deleted without appropriate validation.
- A deleted record should not be recoverable unless under specific circumstances (e.g., if a deletion was made in error and within a defined period).

