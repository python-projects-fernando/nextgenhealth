# Use Case Specification: Book Appointment

## Basic Information

| **Field** | **Value** |
|---------|---------|
| **Use Case ID** | UC-APP-01 |
| **Use Case Name** | Book Appointment |
| **Primary Actor** | Patient, Nurse, Administrator |
| **Secondary Actors** | Doctor, System (Notification Service, Calendar Service) |
| **Brief Description** | Allows an authenticated user to schedule a new appointment with a doctor, selecting from available time slots based on date, doctor, and appointment type. |
| **Priority** | High (Core functionality for patient engagement) |
| **Status** | Proposed / In Analysis |
| **Module** | Appointment Scheduling |
| **Related Requirements** | REQ-APP-001, REQ-APP-002, REQ-APP-003, REQ-APP-004, REQ-APP-006, REQ-APP-007, REQ-APP-010 |

---

## Preconditions
1. The user (Patient, Nurse, or Administrator) is **logged in** and authenticated.
2. The user has appropriate permissions:
   - Patient: can book for themselves.
   - Nurse/Administrator: can book for any patient.
3. Doctor exists in the system and has defined availability.
4. Internet connection is available.
5. Calendar and notification services are operational.

---

## Postconditions
1. A new appointment is created in the system with status "Scheduled".
2. Appointment is linked to patient, doctor, date, time, type, and duration.
3. Patient receives a confirmation notification (email/SMS).
4. Doctor is notified of the new appointment (within 1 hour).
5. Appointment appears in the user’s and doctor’s calendar views.
6. Audit log records the booking action.

---

## Main Success Scenario (Basic Flow)

| Step | Actor | System |
|------|-------|--------|
| 1 | — | User navigates to "Book Appointment" page. |
| 2 | User | Selects doctor, preferred date, and appointment type (e.g., consultation, follow-up). |
| 3 | System | Retrieves and displays available time slots in real-time (REQ-APP-008). |
| 4 | User | Selects a valid time slot. |
| 5 | User | Confirms appointment details. |
| 6 | System | Validates: <br> - Doctor is available at selected time (REQ-APP-004) <br> - No double-booking (REQ-APP-002) <br> - Patient has no overlapping appointment (REQ-APP-003) |
| 7 | System | Creates appointment record with status "Scheduled". |
| 8 | System | Links appointment to patient, doctor, and user who booked it. |
| 9 | System | Sends confirmation: <br> - Email to patient <br> - SMS reminder scheduled (24h prior) <br> - Notification to doctor (within 1 hour) (REQ-APP-010, REQ-APP-011, REQ-APP-012) |
| 10 | System | Logs booking event in audit trail. |
| 11 | System | Displays success message: "Appointment confirmed for [date] at [time]." |
| 12 | System | Updates doctor’s calendar in real-time. |

---

## Alternative Flows

### **A1 – No Available Time Slots**
- **Trigger**: Step 3 – No slots available for selected date/doctor.
- **Steps**:
  1. System displays message: "No availability found. Please try another date or doctor."
  2. Offers "Suggest Nearby Slots" option (e.g., ±1 day).
- **Resume**: User adjusts selection and retries.

### **A2 – Nurse or Admin Books for Patient**
- **Trigger**: Actor is Nurse or Administrator.
- **Modification**:
  - Step 2: User selects patient from a searchable list.
  - Step 6: System validates patient’s eligibility (active account, no no-show history if policy applies).
  - Step 9: Confirmation sent to patient (not actor).

---

## Exception Flows

### **E1 – Doctor Unavailable at Selected Time**
- **Trigger**: Step 6 – Doctor marked as unavailable (e.g., emergency, vacation).
- **Steps**:
  1. System blocks booking.
  2. Displays: "Doctor is no longer available at this time. Please select another slot."
  3. Refreshes availability.
- **End**: User selects new slot or cancels.

### **E2 – Overlapping Appointment Detected**
- **Trigger**: Step 6 – Patient already has an appointment at the same time.
- **Steps**:
  1. System blocks booking.
  2. Displays: "You have another appointment at this time. Please choose a different slot."
  3. Highlights conflicting appointment.
- **Resume**: User selects new time.

### **E3 – Notification Service Failure**
- **Trigger**: Step 9 – Email or SMS service is down.
- **Steps**:
  1. System logs error.
  2. Proceeds with appointment creation.
  3. Flags notification for retry.
  4. Displays: "Appointment confirmed. Notification may be delayed."
- **Note**: Audit log records partial failure.

---

## Business Rules
- **BR-APP-01**: Appointments can be 15, 30, 45, or 60 minutes.
- **BR-APP-02**: Appointment types: consultation, follow-up, examination.
- **BR-APP-03**: Patients cannot book overlapping appointments.
- **BR-APP-04**: Doctors cannot be double-booked at the same time (REQ-APP-002).
- **BR-APP-05**: Only authenticated users can book appointments.
- **BR-APP-06**: Nurses and admins can book on behalf of patients.

---

## Non-Functional Requirements
| ID | Requirement |
|----|-------------|
| REQ-PERF-002 | Page loads in less than 2 seconds; calendar renders in <1s. |
| REQ-USE-002 | Interface responsive on desktop, tablet, and mobile. |
| REQ-APP-011 | Appointment reminders sent: 48h (email), 24h (SMS). |
| REQ-APP-012 | Doctor notified of new appointment within 1 hour. |
| REQ-SEC-003 | All booking actions logged in audit trail. |

---

## Data Dictionary (Key Fields)

| Field | Type | Required | Validation |
|------|------|----------|-----------|
| Patient | UUID | Yes | Must be active patient |
| Doctor | UUID | Yes | Must be active and available |
| Date | Date | Yes | Future date only |
| Time | Time | Yes | Must match available slot |
| Appointment Type | Enum | Yes | consultation, follow-up, examination |
| Duration | Integer (min) | Yes | 15, 30, 45, 60 |
| Status | String | Auto-set | Scheduled (default) |

---

## Notes and Open Issues
- ✅ Future enhancement: Allow rescheduling during booking (if slot is free).
- 🔔 Patients can cancel up to 24 hours in advance (covered in UC-APP-02_Cancel_Appointment).
- 📱 Mobile view: Critical functions (view, book) must be accessible on smaller screens.

