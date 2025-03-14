# Use Case Specification: **Search**

## 1. Overview

This document specifies the **"Search"** use case for the **NextGenHealth** system. The purpose of this use case is to allow administrators, nurses, and doctors to search for and view patient information and records related to appointments and exams.

---

## 2. Use Case Details

### 2.1 Use Case ID  
**UC-05**: Search

### 2.2 Actors
- **Primary Actor**: Administrator, Nurse, Doctor
- **Secondary Actor**: System (performs the search and displays results)

### 2.3 Preconditions
- The user (administrator, nurse, or doctor) must be authenticated.
- The administrator, nurse, and doctor have permission to search for any patient’s records.
- The patient cannot perform searches and can only view their own profile by clicking the "View Profile" option.

### 2.4 Postconditions
- The search results are displayed on the screen.
- The user (administrator, nurse, or doctor) can select and view the details of the searched record.

### 2.5 Trigger
- The administrator, nurse, or doctor initiates a search from the main page or dashboard by entering search criteria such as name, national ID, email, or other identifiers.

---

## 3. Basic Flow (Main Success Scenario)

### **Administrator, Nurse, or Doctor Searching for Patient Records:**
1. The administrator, nurse, or doctor accesses the search page in the system.
2. The user enters a search criterion, such as name, national ID, or email.
3. The system validates the input and performs the search.
4. The system displays results that correspond to the search, including records of multiple patients.
5. The user (administrator, nurse, or doctor) selects one of the results to view full details about the patient, appointments, exams, or medical records.

---

### Alternative Flow:
- If no results are returned from the search, the system will display a message indicating that no records were found.
- If the search criteria are invalid (e.g., incorrect email format), the system will prompt the user to correct the input.

---

## 4. Special Requirements

- **Access Control:** The administrator, nurse, and doctor can search for any patient’s records. The patient cannot perform searches and can only view their own profile.
- **Efficient Search:** The system must be able to perform quick and accurate searches even with large volumes of data.
- **Search Filters:** Administrators, nurses, and doctors can apply filters to refine search results, such as appointment date, exam type, etc.

---

## 5. Exceptions

- If the system is down or cannot access the database, the system will display an error message.
- If the user attempts to perform a search without providing valid criteria, the system will prompt them to enter at least one search criterion.
- If the user does not have sufficient permissions to perform the search, the system will inform them that the action is prohibited.

---

## 6. Relationships

- **Include:**
  - None

---

## 7. Assumptions

- The administrator, nurse, or doctor has the appropriate permissions to perform the search.
- The system has access to up-to-date and complete patient and medical record data.

---

## 8. Notes

- The system may display auto-completion suggestions as the user types search criteria, making the process faster and more intuitive.
- To improve the experience, search results can be displayed in a paginated format to avoid overwhelming the user with too much information at once.

