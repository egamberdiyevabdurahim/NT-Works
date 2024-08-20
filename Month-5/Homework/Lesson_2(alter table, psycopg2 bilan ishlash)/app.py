from for_print import error, enter, success, prints, command

from User.app import (add_column_to, rename_column, change_datatype_column, delete_column,
                      create_table, rename_table, delete_table,
                      show_all_tables, show_all_columns_from_table, show_users, show_user,
                      create_user, delete_user, login)


def after_login_dev():
    """
    Function to handle after login as developer.
    """
    print(success+"Welcome, Developer!")
    while True:
        print(prints+"Main/AfterLoginDeveloper/")
        print(command + "1. Create Table\n"
                        "2. Rename Table\n"
                        "3. Delete Table\n"
                        "4. Add Column to Table\n"
                        "5. Rename Column\n"
                        "6. Change Column Data Type\n"
                        "7. Remove Column from Table\n"
                        "8. Show All Tables\n"
                        "9. Show All Columns from Table\n"
                        "10. Exit")
        choice: str = input(enter + "Enter: ")

        if choice == "1":
            create_table()

        elif choice == "2":
            rename_table()

        elif choice == "3":
            delete_table()

        elif choice == "4":
            add_column_to()

        elif choice == "5":
            rename_column()

        elif choice == "6":
            change_datatype_column()

        elif choice == "7":
            delete_column()

        elif choice == "8":
            show_all_tables()

        elif choice == "9":
            show_all_columns_from_table()

        elif choice == "10":
            break

        else:
            print(error + "Invalid input.")


def after_login_admin():
    """
    Function to handle after login as admin.
    """
    print(success+"Welcome, Admin!")
    while True:
        print(prints+"Main/AfterLoginAdmin/")
        print(command + "1. Create User\n"
                        "2. Delete User\n"
                        "3. Show All Users\n"
                        "4. Show Male Users\n"
                        "5. Show Female Users\n"
                        "6. LogOut")
        choice: str = input(enter + "Enter: ")

        if choice == "1":
            create_user()

        elif choice == "2":
            delete_user()

        elif choice == "3":
            show_users()

        elif choice == "4":
            show_users(male=True)

        elif choice == "5":
            show_users(female=True)

        elif choice == "6":
            break

        else:
            print(error + "Invalid input.")


def after_login_user(email: str):
    """
    Function to handle after login as user.
    """
    print(success+"Welcome, User!")
    while True:
        print(prints+"Main/AfterLoginUser/")
        print(command + "1. Show Profile\n"
                        "2. Exit")
        choice: str = input(enter + "Enter: ")

        if choice == "1":
            show_user(email)

        elif choice == "2":
            break

        else:
            print(error + "Invalid input.")


def after_login(status, email=None):
    """
    Function to handle after login status.
    """
    if status == "Developer":
        after_login_dev()

    elif status == "Admin":
        after_login_admin()

    elif status == "User":
        after_login_user(email)

    else:
        print(error + "Invalid user status.")


def runner():
    """
    Main function to run the program.
    """
    print("Welcome to MasterPhone's System!")
    while True:
        print(prints+"Main/")
        print(command+"\n1. Register\n"
              "2. Login\n"
              "3. Exit\n")

        choice: str = input(enter+"Enter your choice: ")

        if choice == "1":
            a = create_user()
            if a:
                after_login(status=a[2], email=a[0])

        elif choice == "2":
            a = login()
            if a:
                after_login(a[2], email=a[0])

        elif choice == "3":
            print(success+"Exiting...")
            break

        else:
            print(error+"Invalid choice. Please try again.")


if __name__ == '__main__':
    runner()