from storage import PetStorage


class PetCareSystem:
    """Manages pets, searching, statistics, and saved records."""

    def __init__(self):
        self.pets = []
        self.storage = PetStorage()
        self.load_pets()

    def register_pet(self, pet):
        self.pets.append(pet)
        self.save_pets()

    def display_all_pets(self):
        if not self.pets:
            print("No pets have been registered.")
            return

        for pet in self.pets:
            print("\n" + pet.display_info())
            print("Sound:", pet.make_sound())

    def search_pet(self, name):
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None

    def count_pets(self):
        return len(self.pets)

    def average_age(self):
        if not self.pets:
            return 0
        return sum(pet.age for pet in self.pets) / len(self.pets)

    def save_pets(self):
        return self.storage.save_pets(self.pets)

    def load_pets(self):
        self.pets = self.storage.load_pets()
