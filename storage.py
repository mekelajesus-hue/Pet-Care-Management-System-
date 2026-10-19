import json
import os


class PetStorage:
    """Saves and loads pet records using a JSON file."""

    def __init__(self, filename="pets.json"):
        self.filename = filename

    def save_pets(self, pets):
        """Save the registered pets to a file."""
        try:
            data = []

            for pet in pets:
                data.append({
                    "name": pet.name,
                    "age": pet.age,
                    "type": pet.__class__.__name__,
                    "vaccination_status": pet.health_record.vaccination_status,
                    "medical_notes": pet.health_record.medical_notes
                })

            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return True

        except (OSError, TypeError, ValueError) as error:
            print(f"Error saving pets: {error}")
            return False

    def load_pets(self):
        """Read previously saved pets from a file."""
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("The pet data must be a list.")

            pets = []

            for item in data:
                if not isinstance(item, dict):
                    raise ValueError("A pet record is invalid.")

                name = item["name"]
                age = item["age"]
                pet_type = item["type"]
                vaccination = item.get("vaccination_status", "Unknown")
                notes = item.get("medical_notes", "None")

                if not isinstance(name, str) or not name.strip():
                    raise ValueError("A pet name is invalid.")

                if isinstance(age, bool) or not isinstance(age, int) or age < 0:
                    raise ValueError("A pet age is invalid.")

                if pet_type == "Dog":
                    from dog import Dog
                    pet = Dog(name, age, vaccination, notes)

                elif pet_type == "Cat":
                    from cat import Cat
                    pet = Cat(name, age, vaccination, notes)

                else:
                    raise ValueError("Unknown pet type in saved data.")

                pets.append(pet)

            return pets

        except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as error:
            print(f"Error loading pets: {error}")
            return []
