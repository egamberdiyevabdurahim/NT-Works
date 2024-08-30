from app import main
from utils.for_company import is_company_username_taken, get_id_from_username

from .super_admin_func import (create_company, delete_company,
                               view_all_companies, view_all_company_employees, view_company_employees)


def after_login_super():
    """
    Function to handle after login actions for super admin.
    """
    print("\nSuper Admin Menu:")
    print("1. Add Company\n"
          "2. Remove Company\n"
          "3. View All Company\n"
          "4. View All Employees\n"
          # "5. View One Company's Employees\n"
          "6. LogOut\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_company()

    elif choice == "2":
        delete_company()

    elif choice == "3":
        view_all_companies()

    elif choice == "4":
        view_all_company_employees()

    # elif choice == "5":
    #     view_all_companies()
    #     company_username = input("Enter Company Username: ")
    #     if not is_company_username_taken(company_username):
    #         print("Company not found.")
    #         return after_login_super()
    #     view_company_employees(company_username)

    elif choice == "6":
        print("Goodbye!")
        return main()

    else:
        print("Invalid choice. Please try again.")

    return after_login_super()
