# 8. Data Dictionary for NextGenHealth

This document provides a data dictionary for the NextGenHealth system, describing the structure, format, and meaning of each data element used in the database.  
It ensures consistency, clarity, and compliance with healthcare data standards.

## 8.1 Conventions

| Symbol | Meaning |
|--------|---------|
| PK     | Primary Key |
| FK     | Foreign Key |
| NN     | Not Null |
| UQ     | Unique Constraint |
| AI     | Auto Increment (if applicable) |
| Format | Data format or validation rules |
| Domain | Allowed values or value range |

## 8.2 Tables and Fields

### 8.2.1 users  
Stores authentication and role data for all system users (Patient, Nurse, Doctor, Administrator).

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| user_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier for the user |
| email | VARCHAR(254) | ❌ | - | ✅ | ✅ | ❌ | RFC 5322 compliant | Login credential; case-insensitive |
| password_hash | TEXT | ❌ | - | ✅ | ❌ | ❌ | bcrypt/scrypt/PBKDF2 | Securely hashed password |
| first_name | VARCHAR(100) | ❌ | - | ✅ | ❌ | ❌ | - | User's first name |
| last_name | VARCHAR(100) | ❌ | - | ✅ | ❌ | ❌ | - | User's last name |
| date_of_birth | DATE | ❌ | - | ❌ | ❌ | ❌ | YYYY-MM-DD | Optional for non-patients |
| gender | VARCHAR(20) | ❌ | - | ❌ | ❌ | ❌ | Male, Female, Other, Prefer not to say | - |
| phone | VARCHAR(20) | ❌ | - | ❌ | ❌ | ❌ | E.164 format | Optional contact number |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Record creation time |
| updated_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Last update time |
| status | VARCHAR(20) | ❌ | - | ✅ | ❌ | ❌ | Active, Inactive, Locked, Pending | Account status |
| role | VARCHAR(20) | ❌ | - | ✅ | ❌ | ❌ | Patient, Nurse, Doctor, Administrator | User role for RBAC |

> 🔹 **Note**: This table is the central identity store. All other user types extend this record via role-based specialization.

---

### 8.2.2 patient_profiles  
Stores clinical and demographic data specific to patients.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| profile_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique profile identifier |
| user_id | UUID | ❌ | users.user_id | ✅ | ✅ | ❌ | UUID v4 | Reference to parent user |
| emergency_contact_name | VARCHAR(200) | ❌ | - | ❌ | ❌ | ❌ | - | Emergency contact full name |
| emergency_contact_phone | VARCHAR(20) | ❌ | - | ❌ | ❌ | ❌ | E.164 | - |
| insurance_info | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Policy number, provider, etc. |
| preferred_language | VARCHAR(50) | ❌ | - | ❌ | ❌ | ❌ | en-US, pt-BR, es-ES | Language preference |
| medical_history_summary | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Chronic conditions, allergies, surgeries |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | - |
| updated_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | - |

> 🔹 **Note**: Linked to `users` via `user_id`. Ensures one-to-one relationship between user account and patient data.

---

### 8.2.3 doctor_profiles  
Stores professional information specific to doctors.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| profile_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier |
| user_id | UUID | ❌ | users.user_id | ✅ | ✅ | ❌ | UUID v4 | Reference to user account |
| specialty | VARCHAR(100) | ❌ | - | ✅ | ❌ | ❌ | e.g., Cardiology, Pediatrics | Medical specialty |
| license_number | VARCHAR(50) | ✅ | - | ✅ | ✅ | ❌ | Country-specific format | Professional license ID |
| years_of_experience | INTEGER | ❌ | - | ❌ | ❌ | ❌ | ≥0 | Years in practice |
| bio | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Professional biography |
| availability_schedule | JSONB | ❌ | - | ✅ | ❌ | ❌ | Structured JSON | Weekly working hours and breaks |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Record creation time |
| updated_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Last update time |

> 🔹 **Note**: Doctors are users with extended professional data. The `availability_schedule` drives appointment booking logic.

---

### 8.2.4 nurse_profiles  
Stores operational and professional data for nurses.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| profile_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier |
| user_id | UUID | ❌ | users.user_id | ✅ | ✅ | ❌ | UUID v4 | Reference to user account |
| certification_type | VARCHAR(100) | ❌ | - | ✅ | ❌ | ❌ | RN, LPN, NP, etc. | Nursing certification |
| certification_number | VARCHAR(50) | ✅ | - | ✅ | ✅ | ❌ | Country-specific | Certification ID |
| department | VARCHAR(100) | ❌ | - | ❌ | ❌ | ❌ | e.g., ICU, ER, Pediatrics | Primary unit of work |
| shift_preferences | JSONB | ❌ | - | ❌ | ❌ | ❌ | Structured JSON | Preferred shifts/days |
| emergency_contact_name | VARCHAR(200) | ❌ | - | ❌ | ❌ | ❌ | - | For workplace safety |
| emergency_contact_phone | VARCHAR(20) | ❌ | - | ❌ | ❌ | ❌ | E.164 | - |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Record creation time |
| updated_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Last update time |

> 🔹 **Note**: Nurses are authenticated users with role-specific operational data.

---

### 8.2.5 appointments  
Stores appointment scheduling data.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| appointment_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier |
| patient_user_id | UUID | ❌ | users.user_id | ✅ | ❌ | ❌ | UUID v4 | FK to patient (role = Patient) |
| doctor_user_id | UUID | ❌ | users.user_id | ✅ | ❌ | ❌ | UUID v4 | FK to doctor (role = Doctor) |
| start_time | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Appointment start |
| duration_minutes | INTEGER | ❌ | - | ✅ | ❌ | ❌ | 15, 30, 45, 60 | Duration of visit |
| type | VARCHAR(50) | ❌ | - | ✅ | ❌ | ❌ | Consultation, Follow-up, Examination | Appointment type |
| status | VARCHAR(20) | ❌ | - | ✅ | ❌ | ❌ | Scheduled, Confirmed, Completed, Cancelled | Current state |
| reason_for_visit | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Chief complaint or purpose |
| created_by_user_id | UUID | ❌ | users.user_id | ✅ | ❌ | ❌ | UUID v4 | Who booked the appointment |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Booking timestamp |
| updated_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Last modification |

---

### 8.2.6 medical_records  
Stores electronic medical records linked to appointments.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| record_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier |
| appointment_id | UUID | ❌ | appointments.appointment_id | ✅ | ❌ | ❌ | UUID v4 | Parent appointment |
| doctor_user_id | UUID | ❌ | users.user_id | ✅ | ❌ | ❌ | UUID v4 | Physician responsible |
| chief_complaint | TEXT | ❌ | - | ✅ | ❌ | ❌ | - | Patient's primary concern |
| history_of_present_illness | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Detailed symptom timeline |
| physical_exam_findings | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Clinical observations |
| assessment_diagnosis | TEXT | ❌ | - | ✅ | ❌ | ❌ | - | Medical evaluation |
| treatment_plan | TEXT | ❌ | - | ✅ | ❌ | ❌ | - | Recommended care |
| follow_up_instructions | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Next steps for patient |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Record creation |
| updated_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Last update |

---

### 8.2.7 prescriptions  
Stores digital prescriptions issued during visits.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| prescription_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier |
| record_id | UUID | ❌ | medical_records.record_id | ✅ | ❌ | ❌ | UUID v4 | Source medical record |
| medication_name | VARCHAR(200) | ❌ | - | ✅ | ❌ | ❌ | - | Generic or brand name |
| dosage | VARCHAR(100) | ❌ | - | ✅ | ❌ | ❌ | e.g., "10mg", "5mL" | Amount per dose |
| frequency | VARCHAR(100) | ❌ | - | ✅ | ❌ | ❌ | e.g., "twice daily", "BID" | How often |
| duration_days | INTEGER | ❌ | - | ✅ | ❌ | ❌ | >0 | Number of days to take |
| instructions | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Special directions |
| prescribed_by_user_id | UUID | ❌ | users.user_id | ✅ | ❌ | ❌ | UUID v4 | Doctor who issued it |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Issue timestamp |

---

### 8.2.8 audit_logs  
Critical for HIPAA/GDPR compliance. Logs all sensitive actions.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| log_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier |
| action | VARCHAR(100) | ❌ | - | ✅ | ❌ | ❌ | Create, Update, Delete, Login, Access | Type of event |
| user_id | UUID | ❌ | users.user_id | ✅ | ❌ | ❌ | UUID v4 | Who performed the action |
| target_entity_type | VARCHAR(50) | ❌ | - | ✅ | ❌ | ❌ | User, Appointment, MedicalRecord | What was affected |
| target_entity_id | UUID | ❌ | - | ✅ | ❌ | ❌ | UUID v4 | ID of affected entity |
| details | JSON | ❌ | - | ❌ | ❌ | ❌ | Structured data | Additional context |
| ip_address | INET | ❌ | - | ❌ | ❌ | ❌ | IPv4/IPv6 | Origin IP |
| user_agent | TEXT | ❌ | - | ❌ | ❌ | ❌ | - | Browser/device info |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | Event timestamp |

---

### 8.2.9 notifications  
Tracks sent notifications for reliability and auditing.

| Field Name | Type | PK | FK | NN | UQ | AI | Format | Domain / Description |
|------------|------|----|----|----|----|----|--------|------------------------|
| notification_id | UUID | ✅ | - | ✅ | ✅ | ❌ | UUID v4 | Unique identifier |
| user_id | UUID | ❌ | users.user_id | ✅ | ❌ | ❌ | UUID v4 | Recipient |
| type | VARCHAR(50) | ❌ | - | ✅ | ❌ | ❌ | Email, SMS, InApp | Delivery method |
| subject | VARCHAR(200) | ❌ | - | ❌ | ❌ | ❌ | - | Email subject or SMS preview |
| body | TEXT | ❌ | - | ✅ | ❌ | ❌ | - | Message content |
| status | VARCHAR(20) | ❌ | - | ✅ | ❌ | ❌ | Sent, Failed, Pending | Delivery status |
| sent_at | TIMESTAMP | ❌ | - | ❌ | ❌ | ❌ | ISO 8601 | When delivered |
| created_at | TIMESTAMP | ❌ | - | ✅ | ❌ | ❌ | ISO 8601 | When queued |

---

## 8.3 Indexing Strategy

| Table | Indexed Columns | Purpose |
|------|------------------|--------|
| `users` | `email`, `status`, `role` | Fast login and role-based queries |
| `appointments` | `patient_user_id`, `doctor_user_id`, `start_time` | Scheduling and calendar views |
| `audit_logs` | `user_id`, `action`, `created_at` | Compliance reporting and security audits |
| `medical_records` | `appointment_id`, `doctor_user_id` | Clinical workflow access |

---

## 8.4 Data Retention Policies

| Table | Retention Period | Reason |
|------|------------------|--------|
| `users` | 7 years after account closure | Legal and compliance (HIPAA/GDPR) |
| `patient_profiles` | 7 years after last activity | Medical record retention |
| `doctor_profiles` | 7 years after deactivation | Professional accountability |
| `nurse_profiles` | 7 years after deactivation | Operational compliance |
| `appointments` | 7 years | Audit and billing history |
| `medical_records` | 7+ years (per jurisdiction) | Legal requirement |
| `audit_logs` | 3 years minimum | Security and compliance |
| `notifications` | 1 year | Operational review |

> 🔐 All sensitive data encrypted at rest. PII anonymized where used for analytics.

## 8.5 Conclusion

The data dictionary provides a complete, consistent, and compliant definition of the NextGenHealth database schema. It supports secure, maintainable development aligned with Clean Architecture and DDD principles.

> **Data Model Confidence Level: 9/10**

Proceed to the next phase: [API Spec](09_api_spec.md)
