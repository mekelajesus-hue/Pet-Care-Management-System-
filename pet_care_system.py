class PetCareSystem:
    """Manages pets. Aggregation: pets can exist independently of this system."""

    def __init__(self):
        self.pets = []

    def register_pet(self, pet):
        self.pets.append(pet)

    def display_all_pets(self):
        if not self.pets:
            print("No pets have been registered.")
            return

        for pet in self.pets:
            print("\n" + pet.display_info())
            # Polymorphism: the correct subclass method runs for each pet.
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
