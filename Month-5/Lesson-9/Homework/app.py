from queries.for_running import if_not_used

from auth.login import login

from user.super_admin.super_admin_menu import statistics_menu


def main():
    print("\n1. Login\n"
          "2. Exit\n")

    print("""
    super admin login&password = super
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        email = login()
        if email == "super":
            print(f"Welcome, {email}!")
            statistics_menu()

        elif email:
            print(f"Welcome, {email['first_name']} {email['last_name']}!")
            print("Menu For You is Coming Soon!")
            return None

    elif choice == '2':
        print("Exiting...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return main()


if __name__ == "__main__":
    if_not_used()
    main()