# Pet Care Management System
## OOP Assignment II — Python

### Problem Statement

The Pet Care Management System manages information about dogs and cats. It allows users to register pets, record their health information, search for pets, display pet details, compare pet ages, and calculate statistics.

The system provides a graphical interface for users to perform the main operations. Pet information is saved to a JSON file and loaded when the application starts, allowing records to persist between sessions.

### Object-Oriented Concepts

- **Inheritance:** Dog and Cat inherit common attributes and behaviour from Pet.
- **Composition:** Each Pet creates and owns a HealthRecord.
- **Aggregation:** PetCareSystem manages a collection of pet objects.
- **Polymorphism:** Dog and Cat override make_sound(). Pet objects can also be compared using the overloaded greater-than operator. HealthRecord supports short and detailed displays through an optional argument.
- **Exception handling:** Invalid input and file-related errors are handled to help prevent the application from stopping unexpectedly.
- **Abstract Data Type:** A Python list stores and manages the collection of pets.

### Main Features

- Register dogs and cats.
- Record vaccination status and medical notes.
- Display registered pets.
- Search for a pet by name.
- Calculate the total number of pets and average age.
- Compare two pets by age.
- Save pet records to a JSON file.
- Load saved pet records when the application starts.
- Use a graphical interface with input fields, buttons, and dialogs.

### Files

- `health_record.py` — health record class.
- `pet.py` — base Pet class and age comparison.
- `dog.py` — Dog subclass.
- `cat.py` — Cat subclass.
- `pet_care_system.py` — collection management, searching, statistics, and storage integration.
- `storage.py` — saving and loading pet records.
- `main.py` — console application.
- `gui.py` — graphical user interface.
- `pets.json` — created when pet records are saved.

### How to Run

The project uses Python 3 and Tkinter for the graphical interface. Run `gui.py` to open the graphical application, or `main.py` to use the console application.

### Assignment II

This version extends Assignment I by adding file input/output, exception handling, a graphical interface, and additional polymorphism examples.
