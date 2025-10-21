from typing import Any, Dict


from user_management.domain.factories import PatientProfileFactory


class RegisterPatientProfileUseCase:


    def __init__(self, patient_profile_repository): # Type hint: UserRepository

        self.patient_profile_repository = patient_profile_repository


    async def execute(self, command):

        # --- STEP 1: Delegate User entity creation to the factory ---

        try:
            patient = PatientProfileFactory.create_from_command(command)

        except Exception as e:
            # Re-raise any domain-specific or validation errors encountered during creation
            raise

        # --- STEP 2: Persist the user using the injected repository ---
        try:
            await self.patient_profile_repository.save(patient)
        except Exception as e:
            # Re-raise repository errors (e.g., database connection issues)
            raise

        # --- STEP 3: Return the created and persisted user ---
        return patient
