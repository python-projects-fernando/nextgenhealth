# 8. Data Dictionary for NextGenHealth

This document provides a **data dictionary** for the **NextGenHealth** system, describing the structure, format, and meaning of each data element used in the database.  
It ensures consistency, clarity, and compliance with healthcare data standards.

---

## 8.1 Conventions

- **PK** = Primary Key  
- **FK** = Foreign Key  
- **NN** = Not Null  
- **UQ** = Unique  
- **AI** = Auto Increment (if applicable)  
- **Format** = Data format/validation rules  
- **Domain** = Allowed values or range  

---

## 8.2 Tables and Fields

### 8.2.1 **users**
Stores authentication and role data for all system users.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| user_id          | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique system identifier for the user |
| email            | VARCHAR(255)| NN, UQ                       | Valid email format                           | User login email |
| password_hash    | TEXT        | NN                           | Hashed (bcrypt/argon2)                       | Encrypted password |
| first_name       | VARCHAR(100)| NN                           | Alphabetic characters                        | User's first name |
| last_name        | VARCHAR(100)| NN                           | Alphabetic characters                        | User's last name |
| role             | VARCHAR(50) | NN                           | {Patient, Doctor, Nurse, Admin}              | User role |
| is_active        | BOOLEAN     | NN, default TRUE             | TRUE/FALSE                                   | Account status |
| created_at       | TIMESTAMP   | NN                           | ISO 8601                                     | Record creation date |
| updated_at       | TIMESTAMP   | NN                           | ISO 8601                                     | Record last update |

---

### 8.2.2 **patients**
Stores demographic and contact details for patients.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| patient_id       | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique patient identifier |
| user_id          | UUID        | FK → users.user_id, NN       | UUID v4                                      | Associated user account |
| date_of_birth    | DATE        | NN                           | YYYY-MM-DD                                   | Patient's birth date |
| gender           | VARCHAR(20) | NN                           | {Male, Female, Other, Prefer not to say}     | Gender |
| phone_number     | VARCHAR(20) | NN                           | E.164 format (+CountryCodeNumber)            | Patient's phone number |
| national_id      | VARCHAR(50) | UQ, NULL                     | Country-specific format                      | Government ID (e.g., CPF, SSN) |
| address_street   | VARCHAR(255)| NN                           | Text                                         | Street address |
| address_city     | VARCHAR(100)| NN                           | Text                                         | City |
| address_state    | VARCHAR(100)| NN                           | Text                                         | State/Province |
| address_postcode | VARCHAR(20) | NN                           | Alphanumeric                                 | Postal code |
| insurance_info   | TEXT        | NULL                         | Text                                         | Health insurance details |
| preferred_lang   | VARCHAR(50) | NULL                         | ISO 639-1 code                               | Preferred language |

---

### 8.2.3 **doctors**
Stores information about healthcare providers.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| doctor_id        | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique doctor identifier |
| user_id          | UUID        | FK → users.user_id, NN       | UUID v4                                      | Associated user account |
| specialty        | VARCHAR(100)| NN                           | Text                                         | Medical specialty |
| license_number   | VARCHAR(50) | NN, UQ                       | Country-specific format                      | Professional license number |
| availability     | JSONB       | NN                           | Structured JSON                              | Weekly working hours |

---

### 8.2.4 **appointments**
Stores scheduling details for appointments.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| appointment_id   | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique appointment identifier |
| patient_id       | UUID        | FK → patients.patient_id, NN | UUID v4                                      | Linked patient |
| doctor_id        | UUID        | FK → doctors.doctor_id, NN   | UUID v4                                      | Linked doctor |
| appointment_date | DATE        | NN                           | YYYY-MM-DD                                   | Appointment date |
| start_time       | TIME        | NN                           | HH:MM (24h)                                  | Start time |
| end_time         | TIME        | NN                           | HH:MM (24h)                                  | End time |
| type             | VARCHAR(50) | NN                           | {Consultation, Follow-up, Examination}      | Appointment type |
| status           | VARCHAR(20) | NN                           | {Scheduled, Confirmed, Completed, Cancelled}| Appointment status |
| notes            | TEXT        | NULL                         | Text                                         | Additional details |

---

### 8.2.5 **medical_records**
Stores patient health records.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| record_id        | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique record identifier |
| patient_id       | UUID        | FK → patients.patient_id, NN | UUID v4                                      | Linked patient |
| doctor_id        | UUID        | FK → doctors.doctor_id, NN   | UUID v4                                      | Linked doctor |
| created_at       | TIMESTAMP   | NN                           | ISO 8601                                     | Record creation timestamp |
| updated_at       | TIMESTAMP   | NN                           | ISO 8601                                     | Last update timestamp |
| chief_complaint  | TEXT        | NN                           | Text                                         | Primary reason for visit |
| history_present  | TEXT        | NULL                         | Text                                         | Present illness history |
| physical_exam    | TEXT        | NULL                         | Text                                         | Examination findings |
| diagnosis        | TEXT        | NULL                         | Text                                         | Diagnosis |
| treatment_plan   | TEXT        | NULL                         | Text                                         | Treatment plan |
| follow_up        | TEXT        | NULL                         | Text                                         | Follow-up instructions |

---

### 8.2.6 **prescriptions**
Stores prescription details.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| prescription_id  | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique prescription identifier |
| record_id        | UUID        | FK → medical_records.record_id, NN | UUID v4                              | Linked medical record |
| medication_name  | VARCHAR(255)| NN                           | Text                                         | Drug name |
| dosage           | VARCHAR(100)| NN                           | Text                                         | Dosage |
| frequency        | VARCHAR(100)| NN                           | Text                                         | Administration frequency |
| duration         | VARCHAR(100)| NN                           | Text                                         | Treatment duration |
| special_instr    | TEXT        | NULL                         | Text                                         | Special instructions |
| signed_by        | UUID        | FK → doctors.doctor_id, NN   | UUID v4                                      | Prescribing doctor |

---

### 8.2.7 **medical_files**
Stores metadata for medical documents and images.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| file_id          | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique file identifier |
| patient_id       | UUID        | FK → patients.patient_id, NN | UUID v4                                      | Linked patient |
| record_id        | UUID        | FK → medical_records.record_id, NULL | UUID v4                                | Linked medical record (optional) |
| file_name        | VARCHAR(255)| NN                           | Text                                         | Original file name |
| file_path        | TEXT        | NN                           | URI                                          | Storage location |
| file_type        | VARCHAR(50) | NN                           | MIME type                                    | File type |
| uploaded_at      | TIMESTAMP   | NN                           | ISO 8601                                     | Upload timestamp |

---

### 8.2.8 **audit_logs**
Stores a history of system activity for compliance.

| Field Name       | Data Type   | Constraints                  | Format / Domain                             | Description |
|------------------|-------------|------------------------------|----------------------------------------------|-------------|
| log_id           | UUID        | PK, NN, UQ                   | UUID v4                                      | Unique log identifier |
| user_id          | UUID        | FK → users.user_id, NN       | UUID v4                                      | User who performed the action |
| action           | VARCHAR(255)| NN                           | Text                                         | Action performed |
| entity           | VARCHAR(255)| NN                           | Text                                         | Affected entity/table |
| entity_id        | UUID        | NULL                         | UUID v4                                      | Identifier of the affected record |
| timestamp        | TIMESTAMP   | NN                           | ISO 8601                                     | When the action occurred |
| details          | TEXT        | NULL                         | JSON/Text                                    | Additional information |

---

## 8.3 Data Privacy and Compliance Notes

- **PII** (Personally Identifiable Information) such as name, email, phone, and national ID will be encrypted at rest and transmitted only via TLS 1.3.
- **PHI** (Protected Health Information) will be handled according to HIPAA and GDPR requirements.
- All access to sensitive data will be logged in **audit_logs**.
- Test data must be anonymized before use in non-production environments.

---

Proceed to the next phase: [API Spec](09_api_spec.md)
