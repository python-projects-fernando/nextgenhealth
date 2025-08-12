# 9. API Specification for NextGenHealth

This document defines the **REST API specification** for the **NextGenHealth** healthcare management system.  
It describes the available endpoints, request/response formats, authentication requirements, and error handling.

---

## 9.1 Overview

- **Base URL**:  
```

[https://api.nextgenhealth.com/v1](https://api.nextgenhealth.com/v1)

````
- **Protocol**: HTTPS only (TLS 1.3).
- **Authentication**: Bearer Token (JWT).
- **Content-Type**: `application/json` for requests and responses.
- **Pagination**:  
- Query parameters: `?page=<int>&limit=<int>`
- Default limit: 20 items.

---

## 9.2 Authentication & Authorization

### 9.2.1 Login
**POST** `/auth/login`  
Authenticates a user and returns a JWT token.

**Request Body**
```json
{
"email": "user@example.com",
"password": "string"
}
````

**Response (200 OK)**

```json
{
  "token": "jwt_token_here",
  "expires_in": 3600
}
```

**Error Codes**

* 401 Unauthorized — Invalid credentials.
* 403 Forbidden — Account inactive.

---

### 9.2.2 Refresh Token

**POST** `/auth/refresh`
Refreshes the JWT token.

---

## 9.3 User Management

### 9.3.1 Create User

**POST** `/users`
Creates a new user account (admin only).

**Request Body**

```json
{
  "email": "string",
  "password": "string",
  "first_name": "string",
  "last_name": "string",
  "role": "Patient"
}
```

**Response (201 Created)** — Returns user details without password.

---

### 9.3.2 Get Current User Profile

**GET** `/users/me`
Returns the authenticated user's profile.

---

## 9.4 Patient Management

### 9.4.1 Create Patient

**POST** `/patients`
Registers a new patient.

**Request Body**

```json
{
  "user_id": "uuid",
  "date_of_birth": "YYYY-MM-DD",
  "gender": "Male",
  "phone_number": "+15551234567",
  "national_id": "string",
  "address_street": "string",
  "address_city": "string",
  "address_state": "string",
  "address_postcode": "string",
  "insurance_info": "string",
  "preferred_lang": "en"
}
```

---

### 9.4.2 Get Patient by ID

**GET** `/patients/{patient_id}`

---

### 9.4.3 Search Patients

**GET** `/patients`
Query params: `?name=string&national_id=string&page=1&limit=20`

---

## 9.5 Doctor Management

### 9.5.1 Create Doctor

**POST** `/doctors`
Registers a new doctor.

---

### 9.5.2 Get Doctor Availability

**GET** `/doctors/{doctor_id}/availability`

---

## 9.6 Appointment Management

### 9.6.1 Create Appointment

**POST** `/appointments`

**Request Body**

```json
{
  "patient_id": "uuid",
  "doctor_id": "uuid",
  "appointment_date": "YYYY-MM-DD",
  "start_time": "HH:MM",
  "end_time": "HH:MM",
  "type": "Consultation",
  "notes": "string"
}
```

---

### 9.6.2 Update Appointment

**PUT** `/appointments/{appointment_id}`

---

### 9.6.3 Cancel Appointment

**DELETE** `/appointments/{appointment_id}`

---

## 9.7 Medical Records

### 9.7.1 Create Medical Record

**POST** `/medical-records`

---

### 9.7.2 Get Medical Record by ID

**GET** `/medical-records/{record_id}`

---

### 9.7.3 Update Medical Record

**PUT** `/medical-records/{record_id}`

---

## 9.8 Prescriptions

### 9.8.1 Create Prescription

**POST** `/prescriptions`

---

### 9.8.2 Get Prescriptions by Record ID

**GET** `/prescriptions?record_id=uuid`

---

## 9.9 Medical Files

### 9.9.1 Upload Medical File

**POST** `/medical-files`
Multipart form-data with file and metadata.

---

### 9.9.2 Download Medical File

**GET** `/medical-files/{file_id}`

---

## 9.10 Reporting

### 9.10.1 Appointment Statistics

**GET** `/reports/appointments?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`

---

## 9.11 Error Handling

All error responses follow a standard format:

```json
{
  "error": "string",
  "message": "string",
  "code": 400
}
```

**Common Status Codes**:

* **200 OK** — Success.
* **201 Created** — Resource created successfully.
* **204 No Content** — Request successful, no response body.
* **400 Bad Request** — Invalid input.
* **401 Unauthorized** — Missing or invalid credentials.
* **403 Forbidden** — Access denied.
* **404 Not Found** — Resource not found.
* **500 Internal Server Error** — Server-side failure.

---


