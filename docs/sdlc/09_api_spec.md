# 9. API Specification for NextGenHealth

This document defines the RESTful API specification for the NextGenHealth system based on the detailed design in [Detailed Design](./06_detailed_design.md). The API follows REST principles with clear resource naming, standard HTTP methods, and consistent response formats.

All endpoints are versioned under `/api/v1/` and secured with JWT-based authentication.

## 9.1 Base URL

```
https://api.nextgenhealth.com/api/v1/
```

## 9.2 Authentication

### 9.2.1 Login
Authenticates a user and returns a JWT token.

- **Endpoint**: `POST /auth/login`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securePassword123!"
  }
  ```
- **Success Response (200 OK)**:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "user": {
      "user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
      "first_name": "John",
      "last_name": "Doe",
      "role": "Doctor"
    }
  }
  ```

### 9.2.2 Refresh Token
Obtains a new access token using a refresh token.

- **Endpoint**: `POST /auth/refresh`
- **Request Body**:
  ```json
  {
    "refresh_token": "eyJhbGciOiJIUzI1NiIs..."
  }
  ```

### 9.2.3 Logout
Invalidates the current session (optional server-side token invalidation).

- **Endpoint**: `POST /auth/logout`
- **Headers**: `Authorization: Bearer <access_token>`

## 9.3 User Management

### 9.3.1 Register User
Registers a new user. Only administrators can register non-patient users.

- **Endpoint**: `POST /users/register`
- **Headers**: `Authorization: Bearer <admin_token>` (required for non-patients)
- **Request Body**:
  ```json
  {
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@clinic.com",
    "password": "StrongPass!2025",
    "role": "Nurse"
  }
  ```
- **Success Response (201 Created)**:
  ```json
  {
    "user_id": "b2c3d4e5-f6g7-8901-h2i3-j4k5l6m7n8o9",
    "email": "jane.smith@clinic.com",
    "role": "Nurse",
    "status": "Active"
  }
  ```

### 9.3.2 Get Current User Profile
Retrieves the authenticated user's basic info and role.

- **Endpoint**: `GET /users/me`
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
    "user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@clinic.com",
    "role": "Doctor",
    "status": "Active",
    "created_at": "2025-01-15T08:30:00Z"
  }
  ```

### 9.3.3 Update User Profile
Updates the authenticated user's profile.

- **Endpoint**: `PUT /users/me`
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "first_name": "Johnathan",
    "phone": "+12125550123"
  }
  ```

### 9.3.4 Search Users
Searches users by name, email, or phone. Access restricted by role.

- **Endpoint**: `GET /users/search?q=john&role=Doctor`
- **Query Parameters**:
  - `q`: Search term (partial match on name/email)
  - `role`: Optional filter (`Patient`, `Nurse`, `Doctor`, `Administrator`)
- **Headers**: `Authorization: Bearer <token>` (requires appropriate permissions)
- **Response (200 OK)**:
  ```json
  [
    {
      "user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@clinic.com",
      "role": "Doctor"
    }
  ]
  ```

## 9.4 Patient Profile Management

### 9.4.1 Create Patient Profile
Creates clinical and demographic data for a patient.

- **Endpoint**: `POST /patients`
- **Headers**: `Authorization: Bearer <admin_or_nurse_token>`
- **Request Body**:
  ```json
  {
    "user_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    "emergency_contact_name": "Carlos Silva",
    "emergency_contact_phone": "+5521987654321",
    "insurance_info": "Amil, Plano Top",
    "preferred_language": "pt-BR"
  }
  ```
- **Success Response (201 Created)**:
  ```json
  {
    "profile_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "user_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    "emergency_contact_name": "Carlos Silva",
    "created_at": "2025-04-05T10:00:00Z"
  }
  ```

### 9.4.2 Get Patient Profile
Retrieves a patient's clinical profile.

- **Endpoint**: `GET /patients/{user_id}`
- **Headers**: `Authorization: Bearer <authorized_token>` (Doctor, Nurse, Admin)
- **Response**:
  ```json
  {
    "profile_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "user_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    "emergency_contact_name": "Carlos Silva",
    "emergency_contact_phone": "+5521987654321",
    "insurance_info": "Amil, Plano Top",
    "medical_history_summary": "Diabetes tipo 2, hipertensão"
  }
  ```

### 9.4.3 Update Patient Profile
Updates a patient's clinical and demographic information.

- **Endpoint**: `PUT /patients/{user_id}`
- **Headers**: `Authorization: Bearer <patient_token>` (own profile) or `<admin/nurse_token>` (full update)
- **Request Body**:
  ```json
  {
    "emergency_contact_name": "Maria Silva",
    "emergency_contact_phone": "+5521999998888",
    "insurance_info": "Bradesco Saúde, Plano Executivo"
  }
  ```
- **Success Response (200 OK)**:
  ```json
  {
    "profile_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "user_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    "emergency_contact_name": "Maria Silva",
    "updated_at": "2025-04-10T16:30:00Z"
  }
  ```

## 9.5 Doctor Profile Management

### 9.5.1 Create Doctor Profile
Creates professional data for a doctor.

- **Endpoint**: `POST /doctors`
- **Headers**: `Authorization: Bearer <admin_token>`
- **Request Body**:
  ```json
  {
    "user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "specialty": "Cardiology",
    "license_number": "CRM-SP12345",
    "years_of_experience": 12,
    "availability_schedule": {
      "monday": ["08:00", "09:00", "10:00"],
      "tuesday": ["14:00", "15:00"]
    }
  }
  ```
- **Success Response (201 Created)**:
  ```json
  {
    "profile_id": "e5f6g7h8-i9j0-k1l2-m3n4-o5p6q7r8s9t0",
    "user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "specialty": "Cardiology",
    "license_number": "CRM-SP12345"
  }
  ```

### 9.5.2 Get Doctor Profile
Retrieves a doctor's professional information.

- **Endpoint**: `GET /doctors/{user_id}`
- **Headers**: `Authorization: Bearer <authorized_token>`
- **Response**:
  ```json
  {
    "profile_id": "e5f6g7h8-i9j0-k1l2-m3n4-o5p6q7r8s9t0",
    "user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "specialty": "Cardiology",
    "license_number": "CRM-SP12345",
    "availability_schedule": {
      "monday": ["08:00", "09:00", "10:00"],
      "tuesday": ["14:00", "15:00"]
    }
  }
  ```

### 9.5.3 Update Doctor Profile
Updates a doctor's professional information.

- **Endpoint**: `PUT /doctors/{user_id}`
- **Headers**: `Authorization: Bearer <admin_token>` (full update) or `<doctor_token>` (limited fields)
- **Request Body**:
  ```json
  {
    "specialty": "Neurology",
    "availability_schedule": {
      "wednesday": ["10:00", "11:00", "14:00"]
    }
  }
  ```
- **Success Response (200 OK)**:
  ```json
  {
    "profile_id": "e5f6g7h8-i9j0-k1l2-m3n4-o5p6q7r8s9t0",
    "user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "specialty": "Neurology",
    "updated_at": "2025-04-10T17:15:00Z"
  }
  ```

## 9.6 Nurse Profile Management

### 9.6.1 Create Nurse Profile
Creates operational data for a nurse.

- **Endpoint**: `POST /nurses`
- **Headers**: `Authorization: Bearer <admin_token>`
- **Request Body**:
  ```json
  {
    "user_id": "b2c3d4e5-f6g7-8901-h2i3-j4k5l6m7n8o9",
    "certification_type": "RN",
    "certification_number": "COREN-RJ67890",
    "department": "ICU",
    "shift_preferences": ["morning", "night"]
  }
  ```
- **Success Response (201 Created)**:
  ```json
  {
    "profile_id": "f6g7h8i9-j0k1-l2m3-n4o5-p6q7r8s9t0u1",
    "user_id": "b2c3d4e5-f6g7-8901-h2i3-j4k5l6m7n8o9",
    "certification_type": "RN",
    "department": "ICU"
  }
  ```

### 9.6.2 Get Nurse Profile
Retrieves a nurse's professional information.

- **Endpoint**: `GET /nurses/{user_id}`
- **Headers**: `Authorization: Bearer <authorized_token>`
- **Response**:
  ```json
  {
    "profile_id": "f6g7h8i9-j0k1-l2m3-n4o5-p6q7r8s9t0u1",
    "user_id": "b2c3d4e5-f6g7-8901-h2i3-j4k5l6m7n8o9",
    "certification_type": "RN",
    "department": "ICU",
    "shift_preferences": ["morning", "night"]
  }
  ```

### 9.6.3 Update Nurse Profile
Updates a nurse's operational information.

- **Endpoint**: `PUT /nurses/{user_id}`
- **Headers**: `Authorization: Bearer <admin_token>` (only admins can update)
- **Request Body**:
  ```json
  {
    "department": "Pediatrics",
    "shift_preferences": ["day"]
  }
  ```
- **Success Response (200 OK)**:
  ```json
  {
    "profile_id": "f6g7h8i9-j0k1-l2m3-n4o5-p6q7r8s9t0u1",
    "user_id": "b2c3d4e5-f6g7-8901-h2i3-j4k5l6m7n8o9",
    "department": "Pediatrics",
    "updated_at": "2025-04-10T17:30:00Z"
  }
  ```

## 9.7 Doctor Availability

### 9.7.1 Get Available Time Slots
Retrieves available time slots for a doctor on a specific date.

- **Endpoint**: `GET /doctors/{doctor_id}/availability?date=2025-04-10`
- **Query Parameters**:
  - `date`: Date in `YYYY-MM-DD` format
- **Headers**: `Authorization: Bearer <access_token>` (any authenticated user)
- **Response (200 OK)**:
  ```json
  {
    "doctor_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "date": "2025-04-10",
    "available_slots": [
      "09:00", "09:30", "10:00", "14:30", "15:00"
    ]
  }
  ```

## 9.8 Appointment Management

### 9.8.1 Create Appointment
Books a new appointment.

- **Endpoint**: `POST /appointments`
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "patient_user_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    "doctor_user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "start_time": "2025-04-10T09:00:00Z",
    "duration_minutes": 30,
    "type": "Consultation",
    "reason_for_visit": "Annual check-up"
  }
  ```
- **Success Response (201 Created)**:
  ```json
  {
    "appointment_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "patient_user_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    "doctor_user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "start_time": "2025-04-10T09:00:00Z",
    "duration_minutes": 30,
    "type": "Consultation",
    "status": "Scheduled",
    "created_at": "2025-04-05T14:20:00Z"
  }
  ```

### 9.8.2 Get Appointment by ID
Retrieves a specific appointment.

- **Endpoint**: `GET /appointments/{appointment_id}`
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
    "appointment_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "patient_user_id": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
    "doctor_user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "start_time": "2025-04-10T09:00:00Z",
    "duration_minutes": 30,
    "type": "Consultation",
    "status": "Scheduled",
    "reason_for_visit": "Annual check-up",
    "created_at": "2025-04-05T14:20:00Z",
    "updated_at": "2025-04-05T14:20:00Z"
  }
  ```

### 9.8.3 Update Appointment Status
Updates the status of an appointment (e.g., from Scheduled to Cancelled).

- **Endpoint**: `PUT /appointments/{appointment_id}`
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
    "status": "Cancelled",
    "reason": "Patient no-show"
  }
  ```

### 9.8.4 List Appointments for Patient
Lists all appointments for a specific patient.

- **Endpoint**: `GET /patients/{patient_user_id}/appointments`
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  [
    {
      "appointment_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
      "doctor_user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
      "start_time": "2025-04-10T09:00:00Z",
      "type": "Consultation",
      "status": "Scheduled"
    }
  ]
  ```

## 9.9 Electronic Medical Records (EMR)

### 9.9.1 Create Medical Record
Creates a new medical record linked to an appointment.

- **Endpoint**: `POST /medical-records`
- **Headers**: `Authorization: Bearer <doctor_token>`
- **Request Body**:
  ```json
  {
    "appointment_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "chief_complaint": "Headache for 3 days",
    "assessment_diagnosis": "Migraine",
    "treatment_plan": "Prescribe medication and rest"
  }
  ```
- **Success Response (201 Created)**:
  ```json
  {
    "record_id": "e5f6g7h8-i9j0-k1l2-m3n4-o5p6q7r8s9t0",
    "appointment_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "doctor_user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "chief_complaint": "Headache for 3 days",
    "assessment_diagnosis": "Migraine",
    "treatment_plan": "Prescribe medication and rest",
    "created_at": "2025-04-10T10:15:00Z"
  }
  ```

### 9.9.2 Get Medical Record by ID
Retrieves a specific medical record.

- **Endpoint**: `GET /medical-records/{record_id}`
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
    "record_id": "e5f6g7h8-i9j0-k1l2-m3n4-o5p6q7r8s9t0",
    "appointment_id": "d4e5f6g7-h8i9-j0k1-l2m3-n4o5p6q7r8s9",
    "doctor_user_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "chief_complaint": "Headache for 3 days",
    "assessment_diagnosis": "Migraine",
    "treatment_plan": "Prescribe medication and rest",
    "created_at": "2025-04-10T10:15:00Z",
    "updated_at": "2025-04-10T10:15:00Z"
  }
  ```

## 9.10 Error Response Format

All error responses follow a standard format:

```json
{
  "error": "string",
  "message": "string",
  "code": 400
}
```

### Common Status Codes

| Code | Meaning | Description |
|------|--------|-------------|
| `200` | OK | Success |
| `201` | Created | Resource created successfully |
| `204` | No Content | Request successful, no response body |
| `400` | Bad Request | Invalid input |
| `401` | Unauthorized | Missing or invalid credentials |
| `403` | Forbidden | Access denied |
| `404` | Not Found | Resource not found |
| `500` | Internal Server Error | Server-side failure |

## 9.11 Security Considerations

- **Authentication**: JWT tokens with short expiration (1 hour) + refresh tokens (7 days)
- **Authorization**: Role-Based Access Control (RBAC) enforced on every endpoint
- **Data Protection**: All sensitive data encrypted at rest and in transit (TLS 1.3)
- **Rate Limiting**: Prevent abuse (e.g., 100 requests/minute per IP)
- **Audit Logging**: All critical actions logged in `audit_logs`

## 9.12 Versioning Strategy

- **URL Versioning**: `/api/v1/...`
- **Backward Compatibility**: Breaking changes require new major version
- **Deprecation Policy**: Old versions supported for 6 months after new release

## 9.13 Conclusion

The API specification provides a secure, scalable, and well-documented interface for the NextGenHealth system. It aligns with:
- Clean Architecture
- Domain-Driven Design
- Healthcare compliance (HIPAA/GDPR)
- Modern web standards

> **API Design Confidence Level: 9/10**

