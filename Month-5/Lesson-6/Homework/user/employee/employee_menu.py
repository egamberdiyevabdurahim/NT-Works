from .employee_func import *


def after_login_employee(username: str):
    """
    Function to handle the after-login actions for employee.
    """
    print("\n1. Start Work\n"
          "2. End Work\n"
          "3. Show My Statistics\n"
          "4. Show My Data\n"
          "5. Change Password\n"
          "6. LogOut\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        start_work(username)

    elif choice == "2":
        stop_work(username)

    elif choice == "3":
        view_my_statistics(username)

    elif choice == "4":
        show_my_data(username)

    elif choice == "5":
        change_password(username)

    elif choice == "6":
        print("Goodbye!")
        return None

    else:
        print("Invalid choice. Please try again.")

    return after_login_employee(username)