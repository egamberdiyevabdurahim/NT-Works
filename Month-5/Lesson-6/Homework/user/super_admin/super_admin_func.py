from utils.for_company import is_company_username_taken
from utils.printer import company_printer, employee_printer
from queries.for_company import delete_company as dc, insert_company, get_all_companies, get_all_company_employees, get_company_employees


def create_company() -> None:
    company_name: str = input("Enter Company Name: ")
    while not company_name:
        print("Invalid Company Name. Please enter a non-empty string.")
        company_name = input("Re-Enter Company Name: ")

    username: str = input("Enter username: ")
    while is_company_username_taken(username):
        print("Username already taken. Please enter a unique username.")
        username = input("Re-Enter username: ")

    password: str = input("Enter password: ")
    while not password:
        print("Invalid password. Please enter a non-empty string.")
        password = input("Re-Enter password: ")

    insert_company(company_name, username, password)
    print("Company created successfully.")
    return None


def delete_company():
    company_username = input("Enter Company Username: ")
    if not is_company_username_taken(company_username):
        print("Company not found.")
        return None

    dc(company_username)
    print("Company deleted successfully.")
    return None


def view_all_companies() -> None:
    data_of_companies = get_all_companies()
    if data_of_companies == list():
        print("No companies found.")
        return None

    for company in data_of_companies:
        company_printer(company)
        print("-" * 20)
    return None


def view_all_company_employees() -> None:
    data_of_employees = get_all_company_employees()
    if data_of_employees == list():
        print("No employees found!")
        return None

    for employee in data_of_employees:
        employee_printer(employee)
        print("-" * 20)

    return None


def view_company_employees(username: str) -> None:
    data_of_employees = get_company_employees(username)
    if data_of_employees == list():
        print("No employees found for this company!")
        return None

    if data_of_employees is None:
        print("Company not found.")
        return None

    for employee in data_of_employees:
        employee_printer(employee)
        print("-" * 20)

    return None