from health_record import HealthRecord


class Pet:
    """Base class for all pets."""

    def __init__(self, name, age, vaccination_status="Unknown", medical_notes="None"):
        self.name = name
        self.age = age
        self.health_record = HealthRecord(vaccination_status, medical_notes)

    def make_sound(self):
        """Overridden by subclasses to demonstrate polymorphism."""
        raise NotImplementedError("Subclasses must implement make_sound()")

    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"{self.health_record.display_record(detailed=True)}"
        )

    def __gt__(self, other):
        """Allow two pets to be compared by age using >."""
        if not isinstance(other, Pet):
            return NotImplemented
        return self.age > other.age
