# Use Case Specification: Register User

## Basic Information

| Field | Value |
|-------|-------|
| **Use Case ID** | UC-PAT-01 |
| **Use Case Name** | Register User |
| **Primary Actor** | Patient, Administrator |
| **Secondary Actors** | System (Authentication, Audit Logger) |
| **Brief Description** | Allows a patient to self-register or an administrator to register any user (Patient, Nurse, Doctor, Administrator) into the NextGenHealth system, creating both authentication and profile records. |
| **Priority** | High (Mandatory for MVP) |
| **Status** | Finalized / Approved |
| **Module** | User Management |
| **Related Requirements** | REQ-AUTH-001, REQ-AUTH-004, REQ-AUTH-005, REQ-AUTH-006, REQ-PAT-001, REQ-PAT-002, REQ-PAT-003, REQ-PAT-004, REQ-PAT-005, REQ-DATA-004 |

---

## Detailed Description

### Goal in Context
Enable secure registration of users with appropriate roles while maintaining auditability and compliance with healthcare regulations (HIPAA/GDPR).

### Scope
User Management module within the NextGenHealth system.

### Level
User goal

### Preconditions
- For self-registration: The user is not logged in.
- For admin registration: The administrator is authenticated and has valid permissions (`role = Administrator`).
- Internet connection is available.
- Email service is operational (for confirmation, if applicable).

### Postconditions
- A new user record is created in the system.
- A unique internal identifier (`UUID`) is generated and associated with the user.
- Login credentials are created (if self-registration).
- User data is stored securely with encryption at rest.
- Audit log entry is created for the registration action.
- Role-based access control (RBAC) policies are applied based on assigned role.

---

## Main Success Scenario (Basic Flow)

| Step | Actor | System |
|------|-------|--------|
| 1 | — | Displays registration form (web interface). |
| 2 | User (Patient or Admin) | Enters required information: full name, date of birth, gender, email, phone number, address (street, city, state, postal code). |
| 3 | User | Selects or specifies **user role**: `Patient`, `Nurse`, `Doctor`, or `Administrator`. <br> *(Note: Only administrators can register non-patient roles.)* |
| 4 | User | Optionally enters: national ID, emergency contact, insurance information (patients), specialty/license (doctors), certification (nurses). |
| 5 | User | Submits the form. |
| 6 | System | Validates email format (RFC 5322 compliant). |
| 7 | System | Checks for duplicate registration using email address. |
| 8 | System | If validation passes, generates a unique UUID for the user. |
| 9 | System | Hashes password using secure algorithm (e.g., bcrypt/scrypt). |
| 10 | System | Stores user data in the database:<br> - Core data in `users` table<br> - Role-specific data in respective profile tables (`patient_profiles`, `doctor_profiles`, etc.) |
| 11 | System | Assigns role and enforces RBAC:<br> - Self-registration → `Patient`<br> - Admin registration → specified role |
| 12 | System | Logs the registration event in `audit_logs`:<br> `{ action: "UserRegistered", user_id: "...", performed_by: "...", role: "..." }` |
| 13 | System | Displays success message: _"Registration completed successfully."_ |
| 14 | System | (Optional) Sends welcome email with login instructions via SendGrid/AWS SES. |

---

## Alternative Flows

### A1 – Invalid Email or Phone Format  
**Trigger**: Step 6 – Invalid format detected.  
**Steps**:  
- System displays error: _"Please enter a valid email address and phone number."_  
- Returns to Step 2.  
**Resume**: User corrects data and resubmits.

### A2 – Duplicate Email Detected  
**Trigger**: Step 7 – Email already exists.  
**Steps**:  
- System displays error: _"An account with this email already exists."_  
- Prevents registration.  
**Resume**: User must use a different email or recover existing account.

### A3 – Unauthorized Role Assignment  
**Trigger**: Step 3 – Non-administrator attempts to register a `Doctor`, `Nurse`, or `Administrator`.  
**Steps**:  
- System ignores role selection and defaults to `Patient`.  
- Logs warning in audit trail.  
**Resume**: Registration proceeds as `Patient`.

### A4 – Password Validation Failed  
**Trigger**: Step 9 – Weak password provided.  
**Steps**:  
- System validates against policy: minimum 8 chars, one digit, one special character.  
- If failed, shows: _"Password does not meet security requirements."_  
**Resume**: User enters stronger password.

---

## Business Rules

| ID | Rule |
|----|------|
| BR-PAT-01 | Email address must be unique across all users. |
| BR-PAT-02 | Password must be at least 8 characters long, contain a number and a special character. |
| BR-PAT-03 | UUID is immutable and never exposed directly to end users. |
| BR-PAT-04 | Only administrators can register users with roles other than `Patient`. |
| BR-AUTH-01 | All credentials must be stored using one-way encryption (bcrypt or equivalent). |
| BR-AUTH-02 | Role assignment determines access level; no role escalation without authorization. |

---

## Special Requirements

- 🔒 **Security**: Data encrypted at rest (AES-256), TLS 1.3 in transit.
- 🌐 **Accessibility**: Form complies with WCAG 2.1 AA standards.
- 📱 **Responsive Design**: Usable on mobile devices and tablets.
- 📧 **Email Confirmation**: Optional but recommended for patient accounts.
- 📜 **GDPR/HIPAA Compliance**: Users have right to access, correct, and export their data (REQ-DATA-004, REQ-DATA-006).

---

## Frequency of Use
- Estimated: 50–100 registrations per day during initial rollout.

## Open Issues
- Future enhancement: Allow registration via social login (e.g., Google) — out of scope for now.

## Notes
- This use case replaces the legacy `Register Patient` flow, expanding it to support all user types under a unified identity model.
- Ensures alignment with Clean Architecture and Domain-Driven Design principles.