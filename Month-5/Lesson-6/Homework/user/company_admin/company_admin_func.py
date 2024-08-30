from utils import for_department, printer, additions, create_username_password
from utils.for_company import get_id_from_username
# from utils.auth import get_employees_by_department_id
from queries import auth as q_auth
from queries.for_department import (insert_department, get_all_departments, get_department_by_id, delete_department,
                                    update_department as q_update_department)


def add_department(username: str) -> None:
    """
    Function to add a new department to a company.
    """
    company_id = get_id_from_username(username)

    if company_id is None:
        print("Company not found.")
        return None

    department_name = input("Enter the department name: ")
    insert_department(department_name, company_id)
    print("Department added successfully.")
    return None


def view_departments(username: str) -> None:
    """
    Function to view all departments in a company.
    """
    company_id = get_id_from_username(username)
    if company_id is None:
        print("Company not found.")
        return None

    data_of_departments = get_all_departments(company_id)
    if data_of_departments is None:
        print("No departments found in this company.")
        return None

    for department in data_of_departments:
        printer.department_printer(department)
        print("-" * 20)
    return None


def view_department(username: str) -> None:
    """
    Function to view a specific department in a company.
    """
    company_id = get_id_from_username(username)
    if company_id is None:
        print("Company not found.")
        return None

    view_departments(username)

    department_id = input("Enter the department ID: ")
    if not get_department_by_id(department_id):
        print("Invalid department ID.")
        return None

    data_of_department = get_department_by_id(department_id)
    if data_of_department is None:
        print("Department not found.")
        return None

    printer.department_printer(data_of_department)
    return None


def remove_department(username: str) -> None:
    """
    Function to remove a department from a company.
    """
    company_id = get_id_from_username(username)
    if company_id is None:
        print("Company not found.")
        return None

    view_departments(username)

    department_id = input("Enter the department ID: ")
    if not get_department_by_id(department_id):
        print("Invalid department ID.")
        return None

    delete_department(department_id)
    print("Department removed successfully.")
    return None


def update_department(username: str):
    """
    Function to update a department's name.
    """
    company_id = get_id_from_username(username)
    if company_id == list():
        print("Company not found.")
        return None

    view_departments(username)

    department_id = input("Enter the department ID: ")
    if not get_department_by_id(department_id):
        print("Invalid department ID.")
        return None

    new_name = input("Enter the new department name: ")
    if not get_department_by_id(department_id):
        print("Invalid department ID.")
        return None

    q_update_department(department_id, new_name)
    print("Department updated successfully.")
    return None


# EMPLOYEE

def create_employee(company_username: str):
    """
    Function to create a new employee.
    """
    company_id = get_id_from_username(company_username)
    if company_id is None:
        print("Company not found.")
        return None

    first_name: str = input("Enter First Name: ")
    while not first_name.isalpha():
        print("Invalid First Name\n"
                        "stop for Exit")
        first_name = input("Re-Enter First Name: ")

        if first_name.lower() == "stop":
            break

    last_name: str = input("Enter Last Name: ")
    while not last_name.isalpha():
        print("Invalid Last Name\n"
                        "stop for Exit")
        last_name = input("Re-Enter Last Name: ")

        if last_name.lower() == "stop":
            break

    username, password = create_username_password.create_user()

    view_departments(company_username)

    department_id = input("Enter the department ID: ")
    if not get_department_by_id(department_id):
        print("Invalid department ID.")
        return None

    q_auth.insert_user(first_name, last_name, username, password, department_id)
    return None


def view_employees(company_username: str):
    """
    Function to view all employees in a company.
    """
    company_id = get_id_from_username(company_username)
    if company_id is None:
        print("Company not found.")
        return None

    view_departments(company_username)

    department_id = input("Enter the department ID: ")
    if not get_department_by_id(department_id):
        print("Invalid department ID.")
        return None

    data_of_employees = q_auth.get_employees_by_department_id(department_id)
    if data_of_employees is None:
        print("No employees found in this department.")
        return None

    for employee in data_of_employees:
        printer.employee_printer(employee)
        print("-" * 20)

    return None


def delete_employee(username: str):
    """
    Function to delete an employee from a company.
    """
    view_employees(username)

    employee_id = input("Enter the employee ID: ")
    if not q_auth.get_id(employee_id):
        print("Invalid employee ID.")
        return None

    q_auth.delete_employee(employee_id)
    print("Employee deleted successfully.")
    return None


def update_employee(company_id: str):
    """
    Function to update an employee's details.
    """
    view_employees(company_id)

    employee_id = input("Enter the employee ID: ")
    if not q_auth.get_id(employee_id):
        print("Invalid employee ID.")
        return None

    while True:
        print("\n1. First Name\n"
              "2. Last Name\n"
              "3. Department ID\n"
              "4. Exit\n")
        choice = input("Enter: ")

        if choice == "1":
            first_name = input("Enter new First Name: ")
            q_auth.update_first_name(employee_id, first_name)
            print("First Name updated successfully.")
            break

        elif choice == "2":
            last_name = input("Enter new Last Name: ")
            q_auth.update_last_name(employee_id, last_name)
            print("Last Name updated successfully.")
            break

        elif choice == "3":
            view_departments(company_id)
            department_id = input("Enter new Department ID: ")
            if not get_department_by_id(department_id):
                print("Invalid department ID.")
                break
            q_auth.update_department(employee_id, department_id)
            print("Department ID updated successfully.")
            break

        elif choice == "4":
            break

    return None


def view_all_employees(username: str):
    """
    Function to view all employees in the system.
    """
    id_of_employee = q_auth.get_id_from_username(username)
    data_of_employees = q_auth.get_all_employees(id_of_employee)
    if data_of_employees == list():
        print("No employees found.")
        return None

    for employee in data_of_employees:
        printer.employee_printer(employee)
        print("-" * 20)
    return None
