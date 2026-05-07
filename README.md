# Full-Stack Assessment - Inloops Innovations

This repository contains my submission for the Inloops Innovations Internship Technical Assessment. It is divided into two parts: a RESTful API for Employee Management and a Python script for User Input Validation.

## Technology Stack
* **Language:** Python
* **Framework:** Django, Django REST Framework (DRF)

---

## Section A: Employee Management API
A backend application supporting full CRUD operations for an Employee Management System.

### Key Features
* **Validation:** Enforces unique email addresses for all employees.
* **Soft Delete:** Deleting an employee does not remove the record from the database; instead, it safely updates their status to `INACTIVE`.
* **Filtered Fetching:** By default, fetching employees returns only `ACTIVE` records.

### How to Run Locally
1. Clone this repository.
2. Set up a virtual environment: `python -m venv env`
3. Activate the environment: `env\Scripts\activate` (Windows) or `source env/bin/activate` (Mac/Linux).
4. Install dependencies: `pip install django djangorestframework`
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`
7. Navigate to `http://127.0.0.1:8000/api/employees/` to interact with the API.

---

## Section B: Logic Question (User Input Validation)
A standalone Python script demonstrating data validation using Regular Expressions (`re`). 

### Key Features
* Validates usernames (length and alphanumeric checks).
* Validates standard email formatting.
* Enforces strong password requirements (length, uppercase, lowercase, numbers, and special characters).

### How to Run Locally
Navigate to the root directory and run:
```bash
python input_validation.py