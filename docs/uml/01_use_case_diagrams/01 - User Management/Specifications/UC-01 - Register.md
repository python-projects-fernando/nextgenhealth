# Use Case Specification: **Register**

## 1. Overview

This document specifies the **"Register"** use case for the **NextGenHealth** system. The purpose of this use case is to outline the steps involved in registering a new user or patient, ensuring the user information is captured correctly, and automatically assigning the "Patient" role when a user registers. Additionally, the email verification process must be completed before the registration is finalized.

---

## 2. Use Case Details

### 2.1 Use Case ID
**UC-01**: Register

### 2.2 Actors
- **Primary Actor**: User/Patient, Administrator
- **Secondary Actor**: System (automated role assignment, email verification service)

### 2.3 Preconditions
- The user is not currently registered in the system.
- The user has valid information (name, birthdate, email, etc.) to register.
- A valid email address is required for verification.

### 2.4 Postconditions
- A new user record is created.
- The user’s data is stored in the system.
- The user is assigned the "Patient" role automatically if the actor is a **User/Patient**.
- If the actor is an **Administrator**, the "Patient" role can be manually selected.
- The user must verify their email before completing the registration.

### 2.5 Trigger
- A user clicks the **"Register"** button on the registration page or an **Administrator** initiates a registration for a user.

---

## 3. Basic Flow (Main Success Scenario)

### **User/Patient Registration:**
1. The User/Patient provides required information (name, date of birth, address, email, etc.).
2. The system validates the provided information.
3. The system sends a **verification email** with a unique confirmation link.
4. The user clicks the link in the email to verify their email address.
5. The system confirms the email verification.
6. The system creates a new user record in the database.
7. The system automatically assigns the "Patient" role to the user.
8. A confirmation message is shown to the User/Patient.

### **Administrator Registration:**
1. The Administrator enters the user's information.
2. The system validates the information.
3. The Administrator selects the **"Patient"** role (or another role, if applicable).
4. The system creates the new user record in the database.
5. The system sends an email verification request to the new user.
6. A confirmation message is shown to the Administrator.

### **Email Verification Process:**
1. The system sends an email with a **verification link** to the provided email address.
2. The user clicks the link, confirming their email.
3. The system updates the user status as **"Verified"**.
4. The user is now able to log in and access the system.

### Alternative Flow:
- If the provided information is incomplete or invalid, the system prompts the user to correct the data.
- If the user does not verify their email within a set period (e.g., 24 hours), the system may send a reminder or require re-registration.

---

## 4. Special Requirements

- **Automatic Role Assignment**: When the **User/Patient** registers, the "Patient" role is assigned automatically after email verification.
- **Role Selection by Administrator**: When the **Administrator** registers a user, the "Patient" role is either selected automatically or can be manually assigned by the Administrator.
- **Mandatory Email Verification**: Users cannot log in until they verify their email.

---

## 5. Exceptions

- If the email provided by the user already exists in the system, the system should reject the registration and prompt the user to log in.
- If the user does not verify their email within a defined period, their registration remains incomplete, and they cannot log in.
- If the system experiences an error while saving user data, an error message will be displayed.
- If the verification link is expired, the user must request a new one.

---

## 6. Relationships

- **Include**:
   - The **"Verify Email"** use case is included as a required step before finalizing the registration.
   - The **"Assign Role"** use case is included when registering a user, as the role assignment is part of the registration process.
  
- **Extend**:
   - The registration process may be extended with additional steps, such as optional profile completion.

---

## 7. Assumptions

- The user or administrator has access to the registration page and the necessary permissions.
- The user has a valid email address that is not already registered in the system.
- The email verification process is handled by a third-party service or an internal email module.

---

## 8. Notes

- The automatic role assignment occurs **only after email verification** to ensure valid registrations.
- The **Administrator** may have additional responsibilities for user management, such as assigning other roles or permissions.
- A resend option should be available in case the verification email is lost.

---