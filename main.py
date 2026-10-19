from dog import Dog
from cat import Cat
from pet_care_system import PetCareSystem


class PetCareApp:
    """Console application for the Pet Care Management System."""

    def __init__(self):
        self.system = PetCareSystem()

    def register_pet(self):
        name = input("Pet name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        try:
            age = int(input("Pet age in years: "))
            if age < 0:
                print("Age cannot be negative.")
                return
        except ValueError:
            print("Please enter the age as a whole number.")
            return

        pet_type = input("Type (dog/cat): ").strip().lower()
        vaccination = input("Vaccination status: ").strip() or "Unknown"
        notes = input("Medical notes: ").strip() or "None"

        if pet_type == "dog":
            pet = Dog(name, age, vaccination, notes)
        elif pet_type == "cat":
            pet = Cat(name, age, vaccination, notes)
        else:
            print("Invalid type. Please enter dog or cat.")
            return

        self.system.register_pet(pet)
        print(f"{name} was registered successfully.")

    def show_all_pets(self):
        self.system.display_all_pets()

    def find_pet(self):
        name = input("Enter the pet name to search for: ").strip()
        pet = self.system.search_pet(name)

        if pet:
            print(pet.display_info())
            print("Sound:", pet.make_sound())
        else:
            print("Pet not found.")

    def show_statistics(self):
        print("Total registered pets:", self.system.count_pets())
        print("Average pet age:", round(self.system.average_age(), 2))

    def compare_pets(self):
        first_name = input("Enter the first pet's name: ").strip()
        second_name = input("Enter the second pet's name: ").strip()

        first_pet = self.system.search_pet(first_name)
        second_pet = self.system.search_pet(second_name)

        if first_pet is None or second_pet is None:
            print("One or both pets could not be found.")
            return

        if first_pet > second_pet:
            print(f"{first_pet.name} is older than {second_pet.name}.")
        elif second_pet > first_pet:
            print(f"{second_pet.name} is older than {first_pet.name}.")
        else:
            print("Both pets are the same age.")

    def run(self):
        while True:
            print("\n=== PET CARE MANAGEMENT SYSTEM ===")
            print("1. Register a pet")
            print("2. Display all pets")
            print("3. Search for a pet")
            print("4. Show statistics")
            print("5. Compare two pets by age")
            print("6. Exit")

            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                self.register_pet()
            elif choice == "2":
                self.show_all_pets()
            elif choice == "3":
                self.find_pet()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                self.compare_pets()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose 1-6.")


if __name__ == "__main__":
    PetCareApp().run()
