# Use Case Specification: **Country Management**  

## 1. Overview  

This document specifies the **"Country Management"** use case for the **NextGenHealth** system. The purpose of this use case is to allow administrators to create, update, view, and delete countries in the system, ensuring the system maintains a consistent list of countries for address management and other relevant processes.  

---

## 2. Use Case Details  

### 2.1 Use Case ID  
**UC-09**: Country Management  

### 2.2 Actors  
- **Primary Actor**: Administrator  
- **Secondary Actor**: System (performs actions on data storage and retrieval)  

### 2.3 Preconditions  
- The user must be authenticated and have administrator privileges.  
- The system must be operational and capable of storing and retrieving country data.  
- Countries should be managed by administrators only, ensuring data consistency.  

### 2.4 Postconditions  
- The system updates the country list to reflect any changes made by the administrator.  
- The country details are successfully stored, updated, or deleted in the system.  

### 2.5 Trigger  
- The administrator accesses the country management interface in the system and initiates a country-related action (create, update, or delete).  

---

## 3. Basic Flow (Main Success Scenario)  

### **Creating a New Country:**  
1. The administrator selects the "Create Country" option in the system.  
2. The administrator enters the necessary information for the new country (e.g., country name, code).  
3. The system validates the input (e.g., checks if the country already exists).  
4. The system stores the new country details in the database.  
5. The system confirms the creation of the new country.  

### **Updating an Existing Country:**  
1. The administrator selects the "Update Country" option in the system.  
2. The administrator selects a country from the list of existing countries.  
3. The administrator makes necessary changes to the country details.  
4. The system validates the changes (e.g., checks for duplicates or invalid data).  
5. The system updates the country information in the database.  
6. The system confirms the successful update.  

### **Deleting an Existing Country:**  
1. The administrator selects the "Delete Country" option in the system.  
2. The administrator selects a country from the list of existing countries.  
3. The system checks if the country has any dependent data (e.g., addresses).  
4. If no dependent data exists, the system deletes the country from the database.  
5. The system confirms the successful deletion of the country.  
6. If dependent data exists, the system prompts the administrator to confirm or cancel the deletion.  

### **Viewing Country Information:**  
1. The administrator selects the "View Country" option in the system.  
2. The administrator searches for a country by name or other identifiers.  
3. The system retrieves and displays the country information.  

---

### Alternative Flow:  
- If the country already exists during the creation process, the system displays an error message indicating that the country cannot be created.  
- If the administrator attempts to delete a country with dependent data (e.g., addresses), the system prompts the administrator with a warning message and offers an option to cancel the operation.  
- If the administrator does not have sufficient permissions to access the country management interface, the system denies access and displays an error message.  

---

## 4. Special Requirements  

- **Access Control:** Only administrators can manage countries.  
- **Data Validation:** The system must validate country data for correctness and ensure there are no duplicates when adding new countries.  
- **Error Handling:** The system should provide clear error messages for invalid input, failed actions (e.g., database failure), and permission issues.  

---

## 5. Exceptions  

- If the system is unable to create, update, or delete a country due to a database failure, the system will notify the administrator of the failure and may retry the operation.  
- If the administrator attempts to delete a country with associated addresses or other related data, the system will alert the administrator and prevent the deletion unless the dependent data is handled.  

---


## 6. Assumptions  

- The administrator is trained and has the appropriate permissions to manage countries.  
- The system has a valid country list to begin with and can store country data efficiently.  
- The system is designed to handle countries and their relationships with other entities like address data.  

---

## 7. Notes  

- The system should allow for easy searching and filtering of countries when managing the list.  
- The country data should be stored securely, with backup and recovery procedures in place to ensure no loss of critical information.  

