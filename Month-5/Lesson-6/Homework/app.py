from utils import for_login, for_company, auth
from auth import login
from user.super_admin import super_admin_menu
from user.company_admin import company_admin_menu
from user.employee import employee_menu


def after_login(username: str):
    """
    Function to handle the after-login actions.
    """
    if for_login.is_super_admins_username(username):
        print("Welcome, Super Admin!")
        return super_admin_menu.after_login_super()

    elif for_company.is_company_username_taken(username):
        print("Welcome, Company Admin!")
        return company_admin_menu.after_login_company(username)

    elif auth.is_username_taken(username):
        print("Welcome, Employee!")
        return employee_menu.after_login_employee(username)

    else:
        print("Invalid user.")
        return main()


def main() -> None:
    """
    Main function to run the program.
    """
    print("\n1. Login\n"
          "2. Exit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        username: str = login.login()
        if username:
            after_login(username)
        else:
            main()
    elif choice == "2":
        # Exit the program
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()