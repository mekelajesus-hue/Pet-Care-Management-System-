import tkinter as tk
from tkinter import ttk, messagebox

from dog import Dog
from cat import Cat
from pet_care_system import PetCareSystem


class PetCareGUI:
    """Graphical interface for the Pet Care Management System."""

    def __init__(self, root):
        self.root = root
        self.root.title("Pet Care Management System")
        self.root.geometry("700x600")
        self.root.minsize(600, 500)

        self.system = PetCareSystem()

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.type_var = tk.StringVar(value="Dog")
        self.vaccination_var = tk.StringVar(value="Unknown")
        self.notes_var = tk.StringVar()
        self.search_var = tk.StringVar()

        self.build_interface()
        self.refresh_pet_list()

    def build_interface(self):
        title = ttk.Label(
            self.root,
            text="Pet Care Management System",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=12)

        form = ttk.LabelFrame(self.root, text="Register a Pet", padding=10)
        form.pack(fill="x", padx=15, pady=5)

        ttk.Label(form, text="Pet name:").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(form, textvariable=self.name_var).grid(
            row=0, column=1, sticky="ew", padx=5
        )

        ttk.Label(form, text="Age:").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Entry(form, textvariable=self.age_var).grid(
            row=1, column=1, sticky="ew", padx=5
        )

        ttk.Label(form, text="Pet type:").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Combobox(
            form,
            textvariable=self.type_var,
            values=("Dog", "Cat"),
            state="readonly"
        ).grid(row=2, column=1, sticky="ew", padx=5)

        ttk.Label(form, text="Vaccination:").grid(
            row=3, column=0, sticky="w", pady=4
        )
        ttk.Entry(form, textvariable=self.vaccination_var).grid(
            row=3, column=1, sticky="ew", padx=5
        )

        ttk.Label(form, text="Medical notes:").grid(
            row=4, column=0, sticky="w", pady=4
        )
        ttk.Entry(form, textvariable=self.notes_var).grid(
            row=4, column=1, sticky="ew", padx=5
        )

        form.columnconfigure(1, weight=1)

        ttk.Button(
            form, text="Register Pet", command=self.register_pet
        ).grid(row=5, column=0, columnspan=2, pady=10)

        search_frame = ttk.LabelFrame(
            self.root, text="Search Pets", padding=10
        )
        search_frame.pack(fill="x", padx=15, pady=5)

        ttk.Entry(
            search_frame, textvariable=self.search_var
        ).pack(side="left", fill="x", expand=True, padx=5)

        ttk.Button(
            search_frame, text="Search", command=self.search_pet
        ).pack(side="left", padx=5)

        ttk.Button(
            search_frame, text="Show All", command=self.refresh_pet_list
        ).pack(side="left", padx=5)

        list_frame = ttk.LabelFrame(
            self.root, text="Registered Pets", padding=10
        )
        list_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.pet_list = tk.Listbox(list_frame, height=10)
        self.pet_list.pack(fill="both", expand=True)

        buttons = ttk.Frame(self.root, padding=10)
        buttons.pack(fill="x")

        ttk.Button(
            buttons, text="Statistics", command=self.show_statistics
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons, text="Save Data", command=self.save_data
        ).pack(side="left", padx=5)

        ttk.Button(
            buttons, text="Exit", command=self.root.destroy
        ).pack(side="right", padx=5)

    def register_pet(self):
        name = self.name_var.get().strip()

        if not name:
            messagebox.showerror("Invalid Input", "Please enter a pet name.")
            return

        try:
            age = int(self.age_var.get())

            if age < 0:
                raise ValueError("Age cannot be negative.")

        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Age must be a non-negative whole number."
            )
            return

        pet_type = self.type_var.get()
        vaccination = self.vaccination_var.get().strip() or "Unknown"
        notes = self.notes_var.get().strip() or "None"

        if pet_type == "Dog":
            pet = Dog(name, age, vaccination, notes)
        else:
            pet = Cat(name, age, vaccination, notes)

        try:
            self.system.register_pet(pet)
        except Exception as error:
            messagebox.showerror(
                "Registration Error", f"Could not register pet: {error}"
            )
            return

        messagebox.showinfo("Success", f"{name} was registered successfully.")

        self.name_var.set("")
        self.age_var.set("")
        self.notes_var.set("")
        self.refresh_pet_list()

    def refresh_pet_list(self):
        self.pet_list.delete(0, tk.END)

        for pet in self.system.pets:
            self.pet_list.insert(
                tk.END,
                f"{pet.name} | {pet.__class__.__name__} | "
                f"Age: {pet.age} | Sound: {pet.make_sound()}"
            )

    def search_pet(self):
        name = self.search_var.get().strip()

        if not name:
            messagebox.showwarning(
                "Search", "Please enter a pet name to search for."
            )
            return

        pet = self.system.search_pet(name)

        if pet:
            messagebox.showinfo(
                "Pet Found",
                f"{pet.display_info()}\nSound: {pet.make_sound()}"
            )
        else:
            messagebox.showinfo(
                "Search Results", "No pet with that name was found."
            )

    def show_statistics(self):
        messagebox.showinfo(
            "Pet Statistics",
            f"Total pets: {self.system.count_pets()}\n"
            f"Average age: {self.system.average_age():.2f}"
        )

    def save_data(self):
        if self.system.save_pets():
            messagebox.showinfo(
                "Saved", "Pet records were saved successfully."
            )
        else:
            messagebox.showerror(
                "Save Error", "Pet records could not be saved."
            )


if __name__ == "__main__":
    window = tk.Tk()
    app = PetCareGUI(window)
    window.mainloop()
