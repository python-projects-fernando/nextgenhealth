# Use Case Specification: **Update**

## 1. Overview

This document specifies the **"Update"** use case for the **NextGenHealth** system. The purpose of this use case is to allow users and administrators to update user information while ensuring data integrity and access control.

---

## 2. Use Case Details

### 2.1 Use Case ID
**UC-04**: Update

### 2.2 Actors
- **Primary Actor**: User/Patient, Administrator
- **Secondary Actor**: System (validates data and enforces role-based permissions)

### 2.3 Preconditions
- The user must be authenticated.
- The user must have permission to update their own data.
- The administrator can update any user's information.

### 2.4 Postconditions
- The updated information is stored in the system.
- A confirmation message is displayed.
- If necessary, the system triggers notifications about the update.

### 2.5 Trigger
- A user or administrator initiates an update request from the user profile page or admin dashboard.

---

## 3. Basic Flow (Main Success Scenario)

### **User/Patient Updating Their Own Information:**
1. The user navigates to their profile page.
2. The user edits the desired fields (e.g., name, contact details, address).
3. The system validates the updated data.
4. The system saves the changes to the database.
5. A success message is displayed.

### **Administrator Updating a User’s Information:**
1. The administrator searches for the user.
2. The administrator selects the user’s profile.
3. The administrator updates the necessary fields.
4. The system validates the updated data.
5. The system saves the changes to the database.
6. A success message is displayed.

### Alternative Flow:
- If the provided data is invalid, the system displays an error message and prompts for corrections.
- If the user does not have permission to update a field, the system denies the request and logs the attempt.

---

## 4. Special Requirements

- **Role-based Access Control (RBAC):** Only authorized users can update their own information.
- **Audit Logging:** All updates should be logged for security and compliance purposes.
- **Data Validation:** Ensure all fields follow predefined formats (e.g., email format, phone number validation).

---

## 5. Exceptions

- If the database is unavailable, the system displays an error message.
- If the session expires, the user is prompted to log in again.
- If an unauthorized user attempts to update another user’s data, access is denied.

---

## 6. Relationships

- **Extend**:
   - The **"Verify E-mail"** use case may be triggered if the user updates their email address.
   - The **"Assign Role"** use case may be triggered if the administrator updates the user’s role.

---

## 7. Assumptions

- The user or administrator has the necessary permissions to perform the update.
- The system enforces proper validation and security measures.

---

## 8. Notes

- The system should notify users via email if critical information (e.g., email, phone number) is changed.
- Administrators should only update sensitive data when necessary.
