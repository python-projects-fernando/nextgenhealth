# Use Case Specification: Assign Role

## 1. Overview

This document specifies the **"Assign Role"** use case for the **NextGenHealth** system. The purpose of this use case is to define how roles are assigned to users, either automatically during user registration or manually by an administrator.

---

## 2. Use Case Details

### 2.1 Use Case ID
**UC-03**: Assign Role

### 2.2 Actors
- **Primary Actor**: Administrator
- **Secondary Actor**: System (for automatic role assignment during registration)

### 2.3 Preconditions
- The user must exist in the system.
- The administrator must have the necessary permissions to assign roles.
- If the role assignment is automatic, the registration process must be completed.

### 2.4 Postconditions
- The user is assigned a specific role (e.g., Patient, Doctor, Nurse, Administrator).
- The assigned role determines the user's system permissions.

### 2.5 Trigger
- The administrator initiates the role assignment process.
- The system automatically assigns the **Patient** role when a new user registers.

---

## 3. Basic Flow (Main Success Scenario)

### **Manual Role Assignment (Administrator):**
1. The administrator accesses the user management section.
2. The administrator searches for the user who needs a role assignment.
3. The administrator selects the user and chooses a role from the available options.
4. The system validates the request and updates the user’s role.
5. The system confirms the role assignment to the administrator.

### **Automatic Role Assignment (User Registration):**
1. A user completes the registration process.
2. The system verifies the user's email (via the **Verify E-mail** use case).
3. The system automatically assigns the **Patient** role to the new user.
4. The system updates the user record and finalizes the registration.

---

## 4. Alternative Flows

### **Administrator Reassigns a Role:**
- If a user’s role needs to be changed, the administrator can repeat the assignment process.
- The system logs all role changes for audit purposes.

### **Role Assignment Failure:**
- If the administrator selects an invalid role, the system displays an error message.
- If the system encounters a database error, an appropriate error message is shown.

---

## 5. Special Requirements

- **Automatic Role Assignment for Patients**: When a user registers, the **Patient** role is assigned automatically.
- **Role-Based Access Control (RBAC)**: The system must enforce role-based access to prevent unauthorized role assignments.
- **Audit Logs**: All role assignments and changes should be logged for security and tracking.

---

## 6. Exceptions

- If the administrator does not have permission to assign roles, the system should deny access.
- If the system encounters an issue while saving role changes, an error should be logged and displayed.
- If the email verification is incomplete, the role assignment for a new user should not proceed.

---

## 7. Relationships

- **Extend**:
  - The **"Register"** use case extends this use case for automatic role assignment when a user registers.
- **Include**:
  - The **"Verify E-mail"** use case is included to ensure that the user's email is verified before assigning a role.

---

## 8. Assumptions

- The administrator has the correct privileges to assign roles.
- The system follows predefined role structures without custom role creation.
- The **"Patient"** role is the default for new user registrations.

---

## 9. Notes

- Future iterations of the system may allow custom role definitions and advanced permissions.
- Consider implementing multi-role support if required for complex use cases.
- The system should provide UI feedback to inform users of successful or failed role assignments.

---

