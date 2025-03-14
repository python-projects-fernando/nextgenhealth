# Use Case Specification: **Verify E-mail**

## 1. Overview

This document specifies the **"Verify E-mail"** use case for the **NextGenHealth** system. The purpose of this use case is to ensure that a user's email address is valid before they can complete their registration and access the system. The email verification process is mandatory and applies to all registered users.

---

## 2. Use Case Details

### 2.1 Use Case ID
**UC-02**: Verify E-mail

### 2.2 Actors
- **Primary Actor**: User/Patient, Administrator
- **Secondary Actor**: System (email service handling verification)

### 2.3 Preconditions
- The user has completed the initial registration process.
- The system has generated and sent a verification email to the user's registered email address.

### 2.4 Postconditions
- If successful, the user's email is marked as verified in the system.
- If unsuccessful, the user remains in an unverified state and cannot log in.

### 2.5 Trigger
- The user receives a verification email and clicks the provided link.

---

## 3. Basic Flow (Main Success Scenario)

1. The system generates a unique verification token and sends an email containing a verification link.
2. The user clicks the verification link.
3. The system validates the token and verifies the user's email.
4. The system updates the user's status to "Verified."
5. A confirmation message is displayed to the user.

---

## 4. Alternative Flows

### **4.1 Expired Verification Link**
- If the user clicks an expired verification link, the system displays an error message and provides an option to request a new verification email.

### **4.2 Invalid Verification Token**
- If the user clicks a link with an invalid token, the system displays an error and prompts the user to retry the process.

### **4.3 Resend Verification Email**
- If the user does not receive the verification email, they can request the system to resend it.

---

## 5. Special Requirements

- The verification link should expire after a predefined time (e.g., 24 hours).
- The system should log verification attempts for security purposes.
- Users should have an option to request a new verification email if needed.

---

## 6. Exceptions

- If the email service is down, verification emails cannot be sent.
- If the user fails to verify their email within the expiration period, they must request a new verification link.
- If the user enters an incorrect email during registration, they will not receive the verification email and must update their email address before retrying.

---

## 7. Relationships

- **Included in**:
  - **"Register"** (UC-01): The email verification process is a mandatory step in user registration.
- **Extends**:
  - **None**

---

## 8. Assumptions

- The system has access to a functioning email service for sending verification emails.
- The user has entered a valid email address during registration.
- The verification link is unique and cannot be reused after successful verification.

---

## 9. Notes

- If the email remains unverified, the user cannot log in.
- The system should notify the user if their email is already verified when they attempt to verify again.
- Administrators do not need email verification unless explicitly required by the system's configuration.

---
