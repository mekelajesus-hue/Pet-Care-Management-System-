class HealthRecord:
    """Stores the health information belonging to one pet."""

    def __init__(self, vaccination_status="Unknown", medical_notes="None"):
        self.vaccination_status = vaccination_status
        self.medical_notes = medical_notes

    def display_record(self):
        return (
            f"Vaccination status: {self.vaccination_status}\n"
            f"Medical notes: {self.medical_notes}"
        )
