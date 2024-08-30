from .company_admin_func import (add_department, remove_department, view_departments, view_department, update_department,
                                 create_employee, view_employees, update_employee, view_all_employees, delete_employee)


def manage_departments_menu(username: str):
    """
    Function to handle manage departments menu for company admin.
    """
    print("Welcome, Company Admin!")
    print("Manage Departments Menu:")
    print("1. Add Department\n"
          "2. Remove Department\n"
          "3. Show Department\n"
          "4. Edit Department\n"
          "5. Show All Departments\n"
          "7. Go Back\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_department(username)

    elif choice == "2":
        remove_department(username)

    elif choice == "3":
        view_department(username)

    elif choice == "4":
        update_department(username)

    elif choice == "5":
        view_departments(username)

    elif choice == "7":
        print("Going back to main menu...")
        return after_login_company(username)

    else:
        print("Invalid choice. Please try again.")

    return manage_departments_menu(username)


def manage_employees_menu(username: str):
    """
    Function to handle manage employees menu for company admin.
    """
    print("Welcome, Company Admin!")
    print("Manage Employees Menu:")
    print("1. Add Employee\n"
          "2. Remove Employee\n"
          "3. Show Employee\n"
          "4. Edit Employee\n"
          # "5. Show All Employees\n"
          "6. Go Back\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_employee(username)

    elif choice == "2":
        delete_employee(username)

    elif choice == "3":
        view_employees(username)

    elif choice == "4":
        update_employee(username)

    # elif choice == "5":
    #     view_all_employees(username)

    elif choice == "6":
        print("Going back to main menu...")
        return


def after_login_company(username: str):
    """
    Function to handle the after-login actions for company admin.
    """
    print("1. Manage Departments\n"
          "2. Manage Employees\n"
          "3. Show Statistics\n"
          "4. LogOut\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        manage_departments_menu(username)

    elif choice == "2":
        pass
        manage_employees_menu(username)

    elif choice == "3":
        pass
        # show_statistics()

    elif choice == "4":
        print("Goodbye!")
        return None

    else:
        print("Invalid choice. Please try again.")

    return after_login_company(username)