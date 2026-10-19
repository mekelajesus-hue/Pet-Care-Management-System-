class HealthRecord:
    """Stores the health information belonging to one pet."""

    def __init__(self, vaccination_status="Unknown", medical_notes="None"):
        self.vaccination_status = vaccination_status
        self.medical_notes = medical_notes

    def display_record(self, detailed=False):
        """Display a short or detailed health record."""
        if detailed:
            return (
                "=== Detailed Health Record ===\n"
                f"Vaccination status: {self.vaccination_status}\n"
                f"Medical notes: {self.medical_notes}"
            )

        return f"Vaccination status: {self.vaccination_status}"
