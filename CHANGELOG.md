# NextGenHealth - Project Change Log

This document tracks significant changes to project artifacts, including scope, requirements, architecture, and design decisions.

## 2025-09-12: Use Case Updated – Migrated from Register Patient to Register User with Role-Based Support

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `UC-PAT-01_Register_User.md`  
**Change**:  
- Renamed use case from `UC-PAT-01_Register_Patient.md` → `UC-PAT-01_Register_User.md`  
- Updated primary actor to include both `Patient` (self-registration) and `Administrator` (registration of any user)  
- Expanded scope to support registration of all user roles: `Patient`, `Nurse`, `Doctor`, `Administrator`  
- Clarified that only administrators can assign non-patient roles during registration  
- Updated data model references to align with unified `users` table and role-specific profile tables (`patient_profiles`, `doctor_profiles`, etc.)  
- Added explicit link to audit logging requirement (REQ-PAT-011)  
- Removed outdated focus on "patient" in preconditions, postconditions, and business rules  

**Reason**:  
The system supports multiple authenticated roles under a unified identity model. The previous use case was limited to patient registration, which created a fragmented view of user management. Expanding it to `Register User` ensures consistency with the Clean Architecture, DDD principles, and RBAC design, while supporting future scalability.

**Impact**:  
- Enables secure and auditable registration for all user types  
- Strengthens compliance with HIPAA/GDPR through centralized audit trails  
- Provides a clear foundation for API implementation and frontend development  
- Aligns documentation with actual domain logic and database schema

## 2025-09-11: Domain Model Updated – Refined User Management Structure and Relationships

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `User Management` Domain Model (visual diagram)  
**Change**:  
- Renamed module from `Patient Management` → `User Management` to reflect unified identity model  
- Restructured domain entities to use inheritance:  
  - `User` as base entity  
  - `Patient`, `Nurse`, `Doctor`, and `Administrator` as specializations (subtypes) of `User`  
- Removed redundant association between `Administrator` and `User` ("manages") to avoid implying unnecessary structural relationship  
- Corrected cardinalities:  
  - `User` "1" → "1" `UserCredentials` (was incorrectly *:*)  
  - `User` "1" → "*" `AuditLogTrail` (explicit 1:N for audit events)  
- Removed action-based labels (e.g., "registers", "views", "updates") from associations to maintain purity of domain model  
- Aligned with Clean Architecture and DDD principles: separation of concerns, role-based access via RBAC, not structural links  

**Reason**:  
The system supports multiple authenticated roles under a unified user model. The previous domain model introduced artificial relationships (e.g., `Administrator → User`) and mixed behavioral concepts (actions) with structural design. Removing these ensures the domain reflects only core data relationships, while permissions and workflows are properly handled in Use Cases, Application Layer, and Audit Logs.

**Impact**:  
- Improves architectural clarity and maintainability  
- Prevents misinterpretation during implementation (e.g., creating unnecessary join tables)  
- Strengthens alignment with database schema and API design  
- Supports long-term scalability and compliance through centralized identity management

## 2025-09-11: Use Case Diagram Updated – Migrated from Patient-Centric to User-Centric Model

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `User Management` Use Case Diagram (visual)  
**Change**:  
- Renamed module from `Patient Management` → `User Management`  
- Generalized use cases to reflect all user roles:  
  - `Register Patient` → `Register User`  
  - `View Patient Profile` → `View User Profile`  
  - `Update Patient Profile` → `Update User Profile`  
  - `Search Patient` → `Search User`  
- Updated actor permissions based on role-specific access:  
  - **Administrator**: Can register users, view/update any user profile, search users, and view audit trail  
  - **Nurse**: Can view user profiles, search users, and view audit trail  
  - **Doctor**: Can view user profiles, search users, and view audit trail  
  - **Patient**: Can self-register, view own profile, and update own profile  
- Removed incorrect associations (e.g., Patient cannot search or view audit trail)  
- Clarified that only Administrators can create or modify non-patient accounts  

**Reason**:  
The system supports multiple authenticated roles (Patient, Nurse, Doctor, Administrator), each with distinct responsibilities and security boundaries. The previous diagram incorrectly implied broader access rights (e.g., patients searching users). This update ensures the use case model accurately reflects the intended RBAC (Role-Based Access Control) design, aligning with Clean Architecture, DDD, and compliance requirements (HIPAA/GDPR).

**Impact**:  
- Ensures correct implementation of authorization logic in code  
- Prevents over-permissioning of sensitive operations  
- Supports secure and auditable user management workflows  
- Provides a reliable foundation for frontend UI restrictions and API endpoint protection

## 2025-09-11: README Updated – Enhanced Documentation Links and Aligned with User Management Domain

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `README.md`  
**Change**:  
- Renamed "Patient Management" → "User Management" in key features to reflect all user roles (Patient, Nurse, Doctor, Administrator)  
- Updated architecture layer descriptions to use generic, professional language in English:  
  - **Domain**: "Core business entities and domain rules"  
  - **Application**: "Business logic orchestrators (Use Cases) and service interfaces"  
- Specified Django/Flask as backend stack (removed FastAPI references)  
- Added explicit inclusion of `Nurse` and `Administrator` in role-based access control (RBAC) matrix  
- Expanded documentation links to include all SDLC phases from `01_project_scope.md` to `09_api_spec.md`  
- Improved project overview and maintainers section for clarity  

**Reason**:  
The system supports multiple authenticated roles under a unified identity model. The term "Patient Management" was inconsistent with the actual domain and could mislead stakeholders. Updating the README ensures it serves as an accurate, high-level entry point to the project, aligned with Clean Architecture and DDD principles.

**Impact**:  
Provides a clear, consistent, and professional first impression for new developers, auditors, and stakeholders. Ensures traceability across all project artifacts.

## 2025-09-11: API Specification Updated – Added Profile Management Endpoints for All User Roles

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `09_api_spec.md`  
**Change**:  
- Section 9.4 "Patient Profile Management": Added `POST /patients` (create), `GET /patients/{user_id}` (retrieve), and `PUT /patients/{user_id}` (update)  
- Section 9.5 "Doctor Profile Management": Added `POST /doctors`, `GET /doctors/{user_id}`, and `PUT /doctors/{user_id}` with support for `availability_schedule` and `specialty`  
- Section 9.6 "Nurse Profile Management": Added `POST /nurses`, `GET /nurses/{user_id}`, and `PUT /nurses/{user_id}` with role-specific fields  
- Removed standalone "Patient" entity concept — all users are managed under `users` with specialized profiles  
- Clarified RBAC rules for profile creation and update (e.g., only admins can create doctor/nurse profiles)  
- Updated request/response examples to reflect actual data model from `08_data_dictionary.md`  

**Reason**:  
The system supports multiple authenticated roles (Patient, Nurse, Doctor, Administrator), each requiring specialized data beyond basic user information. The previous API specification was incomplete, missing critical update operations and misaligned with the unified `User Management` domain. Adding full CRUD for role-based profiles ensures consistency between the API contract and the underlying data model.

**Impact**:  
Enables complete lifecycle management of user profiles through RESTful interfaces, improves security through granular access control, and supports future features like dynamic scheduling based on doctor availability or nurse shift planning.

## 2025-09-11: Data Dictionary Updated – Added Doctor and Nurse Profile Tables

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `08_data_dictionary.md`  
**Change**:  
- Section 8.2.3 "doctor_profiles": Added new table to store professional data for doctors (specialty, license_number, availability_schedule)  
- Section 8.2.4 "nurse_profiles": Added new table to store operational data for nurses (certification_type, department, shift_preferences)  
- Removed standalone "patients" table concept — replaced with role-specific profiles linked to central `users` table  
- Clarified relationship between `users` and role-based profile tables (one-to-one)  
- Updated indexing and retention policies to include new tables  

**Reason**:  
The system supports multiple authenticated roles (Patient, Nurse, Doctor, Administrator), each requiring specialized data beyond basic user information. The previous model lacked proper structure for healthcare professionals. Adding dedicated profile tables ensures data integrity, security, and scalability while maintaining a unified identity model through the `users` table.

**Impact**:  
Enables accurate representation of clinical workflows, improves compliance with healthcare data standards, and supports future features like scheduling based on doctor specialty or nurse shift planning.

## 2025-09-11: Test Plan Updated – Aligned with User Management Domain

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `07_test_plan.md`  
**Change**:  
- Section 7.1 "Executive Summary" updated to reflect the shift from "Patient Management" → "User Management"  
- Section 7.3.1 "In Scope": Functional testing for "User Management" expanded to include all roles (Patient, Nurse, Doctor, Administrator)  
- Removed references to standalone "Patient Management" module in test scope and approach  
- Role-based permissions clarified in UAT participants and compliance testing sections  
- Sprint-based testing phases updated to align with unified user model implementation  

**Reason**:  
The system supports multiple authenticated roles under a unified user model. The previous focus on "Patient Management" created a fragmented view of testing scope. Consolidating under "User Management" ensures consistent validation of authentication, authorization, audit logging, and role-specific workflows across all modules.

**Impact**:  
Ensures comprehensive test coverage for all user types, strengthens compliance readiness, and aligns QA strategy with the actual domain model.

## 2025-09-11: Detailed Design Updated – Aligned with User Management Domain

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `06_detailed_design.md`  
**Change**:  
- Section 6.1 "Overview" updated to reflect the shift from "Patient Management" → "User Management"  
- Section 6.2.1 "User Management Module": Expanded to include all user roles (Patient, Nurse, Doctor, Administrator)  
- Removed standalone "Patient Management Module" (6.2.2) — consolidated into User Management context  
- Role-based permissions clarified across workflows and data model  
- Data model summary updated to show `users` as central entity with role-specific extensions (`patients`, `doctors`, etc.)  

**Reason**:  
The system supports multiple authenticated roles under a unified user model. The previous separation of "Patient Management" created architectural redundancy and implied that patients were managed differently at the infrastructure level. Consolidating under `User Management` ensures consistency in authentication, authorization, audit logging, and extensibility.

**Impact**:  
Eliminates duplication, strengthens domain alignment, and simplifies long-term maintenance. Supports HIPAA/GDPR compliance through centralized access control and auditability.

## 2025-09-11: System Architecture Updated – Aligned with User Management Domain

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `05_system_architecture.md`  
**Change**:  
- Section 5.1 "Executive Summary" updated to reflect the shift from "Patient Management" → "User Management"  
- Section 5.3.1 "Bounded Context Map": Bounded contexts updated to include `User Context` as central domain  
- All instances of "patient" in architectural descriptions updated to "user" where applicable  
- Role-based permissions clarified across layer design (Application, Domain, Infrastructure)  
- Technology stack note updated to explicitly support multi-role workflows and unified authentication  

**Reason**:  
The system supports multiple authenticated roles (Patient, Nurse, Doctor, Administrator), all managed under a unified user model. The term "Patient Management" was inconsistent with the actual domain and could lead to incorrect assumptions in design and implementation. "User Management" accurately reflects the scope and enables consistent modeling of authentication, authorization, and audit trails.

**Impact**:  
Ensures alignment between system architecture, business logic, and data model. Supports future scalability and compliance with healthcare regulations (HIPAA/LGPD).

## 2025-09-11: Project Planning Updated – Aligned with User Management Domain

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `04_project_planning.md`  
**Change**:  
- Section 4.1 "Executive Summary" updated to reflect the shift from "Patient Management" → "User Management"  
- Section 4.4.1 "Phase 1: Foundation" updated:  
  - Sprint 3 renamed from "Patient Management Foundation" → "User Management Foundation"  
  - Deliverables and acceptance criteria updated to include all user roles (Patient, Nurse, Doctor, Administrator)  
- Role-based permissions clarified in team responsibilities and training requirements  
- Technology stack note updated to explicitly support multi-role workflows  

**Reason**:  
The system supports multiple authenticated roles (Patient, Nurse, Doctor, Administrator), all managed under a unified user model. The term "Patient Management" was inconsistent with the actual domain and could lead to incorrect assumptions in design and implementation. "User Management" accurately reflects the scope and enables consistent modeling of authentication, authorization, and audit trails.

**Impact**:  
Ensures alignment between project planning, technical implementation, and business requirements. Supports future scalability and compliance with healthcare regulations (HIPAA/LGPD).

## 2025-09-11: Feasibility Analysis Updated – Aligned with User Management Domain

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `03_feasibility_analysis.md`  
**Change**:  
- Section 3.1 "Executive Summary" updated to reflect the shift from "Patient Management" to "User Management"  
- Section 3.2.2 "Architecture Feasibility": Bounded Contexts updated to include `User Management` instead of `Patient Management`  
- Role-based permissions clarified across technical, operational, and economic feasibility sections  
- Phase 1 priorities in 3.9.1 updated to focus on unified user model implementation  

**Reason**:  
The system supports multiple authenticated roles (Patient, Nurse, Doctor, Administrator), all managed under a unified user model. The term "Patient Management" was inconsistent with the actual domain and could lead to incorrect assumptions in design and implementation. "User Management" accurately reflects the scope and enables consistent modeling of authentication, authorization, and audit trails.

**Impact**:  
Ensures alignment between business logic, data model, and access control. Supports future scalability and compliance with healthcare regulations (HIPAA/LGPD).

## 2025-09-11: Requirements Document Updated – Aligned with User Management Domain

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `02_requirements_gathering.md`  
**Change**:  
- Section 2.1.1 renamed from "Patient Management" → "User Management"  
- Subsections updated accordingly:  
  - 2.1.1.1 "User Registration" (was Patient Registration)  
  - 2.1.1.2 "User Profile Management"  
  - 2.1.1.3 "User Search"  
- All instances of "patient" in functional requirements updated to "user" where applicable (e.g., registration, search, audit)  
- Role-based permissions clarified across modules to include Nurse and Administrator actions  

**Reason**:  
The system supports multiple authenticated roles (Patient, Nurse, Doctor, Administrator), all managed under a unified user model. The term "Patient Management" was inconsistent with the actual domain and could lead to incorrect assumptions in design and implementation. "User Management" accurately reflects the scope and enables consistent modeling of authentication, authorization, and audit trails.

**Impact**:  
Ensures alignment between business logic, data model, and access control. Supports future scalability and compliance with healthcare regulations (HIPAA/LGPD).

## 2025-09-11: Scope Document Updated – Renamed "Patient Management" to "User Management"

**Author**: Fernando Antunes de Magalhães  
**Document Affected**: `01_project_scope.md`  
**Change**:  
- Section 1.3.1 renamed from "Patient Management" → "User Management"  
- Content restructured into: User Registration, Authentication, Profile Management  
- Added explicit role-based permissions in 1.3.5  

**Reason**:  
The system manages multiple user roles (Patient, Nurse, Doctor, Administrator), all with authentication, profiles, and audit trails. The term "Patient Management" was too narrow and misleading for the actual scope. "User Management" better reflects the domain and supports future scalability.

**Impact**:  
Aligns with Clean Architecture and DDD principles. Prepares the project for consistent modeling of roles, access control, and auditability across modules.