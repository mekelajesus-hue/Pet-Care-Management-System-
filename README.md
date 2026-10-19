# Pet Care Management System

**OOP Assignment 1 — Python**

## Problem overview
The Pet Care Management System registers dogs and cats, stores their health records, searches for pets, displays pet information, and calculates simple statistics.

## Object-oriented concepts
- **Inheritance:** `Dog` and `Cat` inherit from `Pet`.
- **Composition:** each `Pet` creates and owns a `HealthRecord`.
- **Aggregation:** `PetCareSystem` manages a list of pet objects that can exist independently of the system.
- **Polymorphism:** `Dog` and `Cat` implement `make_sound()` differently.
- **Specific object type:** the console asks whether the user is registering a dog or cat.
- **Basic algorithms:** searching by name, counting pets, and calculating average age.

## Files
- `health_record.py` — health record class
- `pet.py` — parent class
- `dog.py` — Dog subclass
- `cat.py` — Cat subclass
- `pet_care_system.py` — collection management and algorithms
- `main.py` — console application

## How to run
Run `main.py` using Python 3. The program uses only Python's standard features and needs no extra packages.
