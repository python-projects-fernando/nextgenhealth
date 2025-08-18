# Use Case Specification: Register Patient

## Basic Information

| **Field** | **Value** |
|---------|---------|
| **Use Case ID** | UC-PAT-01 |
| **Use Case Name** | Register Patient |
| **Primary Actor** | Patient, Administrator |
| **Secondary Actors** | System (Authentication, Audit Logger) |
| **Brief Description** | Allows a patient to self-register or an administrator to register a new patient into the NextGenHealth system, creating both demographic and authentication records. |
| **Priority** | High (Mandatory for MVP) |
| **Status** | Proposed / In Analysis |
| **Module** | Patient Management |
| **Related Requirements** | REQ-PAT-001, REQ-PAT-002, REQ-PAT-003, REQ-PAT-004, REQ-PAT-005, REQ-PAT-006, REQ-PAT-007, REQ-AUTH-001, REQ-DATA-004 |

---

## Preconditions
1. The user is not logged in (for self-registration).
2. For administrator registration: the administrator is authenticated and has valid permissions.
3. Internet connection is available.
4. Email service is operational (for confirmation, if applicable).

---

## Postconditions
1. A new patient record is created in the system.
2. A unique internal identifier (UUID) is generated and associated with the patient.
3. Login credentials are created (if self-registration).
4. Patient data is stored securely with encryption at rest.
5. Audit log entry is created for the registration action.

---

## Main Success Scenario (Basic Flow)

| Step | Actor | System |
|------|-------|--------|
| 1 | — | Displays registration form (web interface). |
| 2 | User (Patient or Admin) | Enters required information: full name, date of birth, gender, email, phone number, address (street, city, state, postal code). |
| 3 | User | Optionally enters: national ID, emergency contact, insurance information, preferred language. |
| 4 | User | Submits the form. |
| 5 | System | Validates email format. |
| 6 | System | Checks for duplicate registration using email address. |
| 7 | System | If validation passes, generates a unique UUID for the patient. |
| 8 | System | Hashes password (if self-registration) using secure algorithm (e.g., bcrypt). |
| 9 | System | Stores patient data in the database. |
| 10 | System | Assigns default role: **Patient** (if self-registration) or specified role (if registered by admin). |
| 11 | System | Logs the registration event in the audit trail (who, when, how). |
| 12 | System | Displays success message: "Registration completed successfully." |
| 13 | System | (Optional) Sends welcome email with login instructions. |

---

## Alternative Flows

### **A1 – Invalid Email or Phone Format**
- **Trigger**: Step 5 – Invalid format detected.
- **Steps**:
  1. System displays error: "Please enter a valid email address and phone number."
  2. Returns to Step 2.
- **Resume**: User corrects data and resubmits.

### **A2 – Duplicate Email Detected**
- **Trigger**: Step 6 – Email already exists in the system.
- **Steps**:
  1. System displays message: "A patient with this email already exists. Please log in or contact support."
  2. Offers link to **Login** or **Forgot Password**.
- **End**: Registration aborted.

### **A3 – Missing Required Fields**
- **Trigger**: Step 4 – Required fields are empty.
- **Steps**:
  1. System highlights missing fields.
  2. Displays message: "All marked fields are required."
  3. Returns to form.
- **Resume**: User fills missing data and resubmits.

### **A4 – Administrator Registers on Behalf of Patient**
- **Trigger**: Actor is Administrator.
- **Modification**:
  - Step 2: Admin fills all fields, including optional ones.
  - Step 8: No password set (or temporary password sent via secure channel).
  - Step 10: System may mark patient as "pending onboarding."
  - Step 13: Sends email with temporary credentials (if applicable).

---

## Exception Flows

### **E1 – Database Unavailable**
- **Trigger**: Step 9 – Database connection fails.
- **Steps**:
  1. System logs error.
  2. Displays message: "Registration could not be completed. Please try again later."
  3. Data is not saved.
- **End**: Process aborted. Admin notified (if in production).

### **E2 – Audit Log Failure**
- **Trigger**: Step 11 – Audit service is down.
- **Steps**:
  1. System logs error locally.
  2. Proceeds with registration (but flags for recovery).
  3. Alert sent to system administrator.
- **Note**: Audit failure does **not** block registration, but must be resolved.

---

## Business Rules
- **BR-PAT-01**: Email address must be unique across all patients.
- **BR-PAT-02**: Password must be at least 8 characters long, contain a number and a special character.
- **BR-PAT-03**: UUID is immutable and never exposed to end users directly.
- **BR-PAT-04**: Only administrators can register staff members (doctors, nurses).
- **BR-AUTH-01**: All credentials must be stored using one-way encryption (bcrypt or equivalent).

---

## Non-Functional Requirements
| ID | Requirement |
|----|-------------|
| REQ-PERF-002 | Form must load in less than 2 seconds. |
| REQ-SEC-002 | All data encrypted at rest (AES-256) and in transit (TLS 1.3+). |
| REQ-USE-001 | Form must be intuitive, with clear labels and error messages. |
| REQ-USE-005 | Error messages must be user-friendly and actionable. |
| REQ-SEC-003 | Registration attempt must be logged in audit trail. |

---

## Data Dictionary (Key Fields)

| Field | Type | Required | Validation |
|------|------|----------|-----------|
| Full Name | String (50+50) | Yes | Not empty |
| Date of Birth | Date | Yes | Valid date, age ≥ 0 |
| Gender | Enum | Yes | Male, Female, Other, Prefer not to say |
| Email | String (100) | Yes | Unique, valid format |
| Phone | String (20) | Yes | E.164 format preferred |
| Address | Structured | Yes | Street, City, State, Postal Code |
| National ID | String (30) | No | Format varies by country |
| Emergency Contact | String | No | Name and phone |
| Insurance Info | String | No | Free text or structured |
| Preferred Language | String | No | e.g., English, Spanish, Portuguese |
| Password | String | Yes (self-reg) | Min 8 chars, 1 number, 1 special char |

---

## Notes and Open Issues
- ✅ Future enhancement: Allow registration via social login (e.g., Google) — out of scope for now.
- 🔒 GDPR/HIPAA: Patient has right to access, correct, and export data (REQ-DATA-004, REQ-DATA-006).
- 📱 Responsive design required for mobile registration.

