import json
import os
from datetime import datetime

from colorama import Fore, init


init(autoreset=True)

error = Fore.RED
enter = Fore.CYAN
re_enter = Fore.MAGENTA
success = Fore.LIGHTGREEN_EX
prints = Fore.YELLOW
command = Fore.LIGHTCYAN_EX

path = f"{os.path.dirname(os.path.abspath(__file__))}/"


class User:
    def __init__(self, username: str, name: str, born_date, password: str):
        self.username: str = username
        self.name: str = name
        self.born_date = born_date
        self.password: str = password


class CustomOpen:
    def __init__(self, filename: str, mode: str):
        self.filename: str = filename
        self.mode: str = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def read_all_data(filename):
    """
    Read all data from JSON file
    """
    file_path = path + filename
    if os.path.getsize(file_path) > 0:
        with CustomOpen(file_path, "r") as file:
            return json.load(file)
    return {}


def write_data(filename, data):
    file_path = path + filename
    """
    Write data to JSON file
    """
    if os.path.exists(file_path):
        with CustomOpen(file_path, "w") as file:
            json.dump(data, file, indent=4)
            return True


def born_date_validator(born_date: str) -> bool:
    try:
        datetime.strptime(born_date, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def get_or_edit_comm():
    """
    Get or edit command
    I wrote this functions because I used it more than once
    """
    print(command + "1. Get\n"
                    "2. Edit")
    choice: str = input(enter + "Enter: ")
    return choice


def get_data(user):
    """
    Get or edit user's data
    """
    counter = 0
    while True:
        print(command+"1. Get or Edit Username\n"
                      "2. Get or Edit Name\n"
                      "3. Get or Edit Birth Date\n"
                      "4. Get or Edit Password\n"
                      "5. Exit")
        choice: str = input(enter+"Enter: ")
        if choice == "1":
            while True:
                choice = get_or_edit_comm()
                if choice == "1":
                    print(prints+f"Username: {user.username}")
                    break

                elif choice == "2":
                    new_username: str = input(enter+"Enter new username: ")
                    while not new_username:
                        print(error+"Username cannot be empty.\n"
                                    "stop for Exit")
                        new_username: str = input(re_enter+"Re-Enter new username: ")
                        if new_username == "stop":
                            exit()

                    user.username = new_username.lower()
                    counter += 1
                    break

                else:
                    print(error+"Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                choice = get_or_edit_comm()
                if choice == "1":
                    print(prints+f"Name: {user.name}")
                    break

                elif choice == "2":
                    new_name: str = input(enter+"Enter new name: ")
                    while not new_name.isalpha():
                        print(error+"Invalid name format. Please enter again.\n"
                                    "stop for Exit")
                        new_name: str = input(re_enter+"Re-Enter new name: ")
                        if new_name == "stop":
                            exit()

                    user.name = new_name.capitalize()
                    counter += 1
                    break

                else:
                    print(error+"Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                choice = get_or_edit_comm()
                if choice == "1":
                    print(prints+f"Birth Date: {user.born_date.strftime('%d.%m.%Y')}")
                    break

                elif choice == "2":
                    new_born_date: str = input(enter+"Enter new birth date\n"
                                               "Example: 01.01.2008: ")
                    while not born_date_validator(new_born_date):
                        print(error+"Invalid date format. Please enter again.\n"
                                    "stop for Exit")
                        new_born_date: str = input(re_enter+"Re-Enter new birth date\n"
                                                   "Example: 01.01.2008: ")
                        if new_born_date == "stop":
                            exit()

                    user.born_date = datetime.strptime(new_born_date, '%Y-%m-%d')
                    counter += 1
                    break

                else:
                    print(error+"Invalid choice. Please try again.")

        elif choice == "4":
            while True:
                choice = get_or_edit_comm()
                if choice == "1":
                    print(prints+f"Password: {user.password}")
                    break

                elif choice == "2":
                    new_password: str = input(enter+"Enter new password: ")
                    while len(new_password) < 8:
                        print(error+"Password must be at least 8 characters long.\n"
                                    "stop for Exit")
                        new_password: str = input(re_enter+"Re-Enter password: ")
                        if new_password == "stop":
                            exit()

                    user.password = new_password
                    counter += 1
                    break

                else:
                    print(error+"Invalid choice. Please try again.")

        elif choice == "5":
            if counter > 0:
                return user
            return None

        else:
            print(error+"Invalid choice. Please try again.")


def register():
    """
    Create a new user and add it to the users.json file.
    """
    with CustomOpen("users.json", "r"):
        username_in: str = input(enter+"Enter username: ")
        while not username_in:
            print(error+"Username cannot be empty.\n"
                        "stop for Exit")
            username_in: str = input(re_enter+"Re-Enter username: ")
            if username_in == "stop":
                exit()

        name_in: str = input(enter+"Enter name: ")
        while not name_in.isalpha():
            print(error+"Invalid name format. Please enter again.\n"
                        "stop for Exit")
            name_in: str = input(re_enter+"Re-Enter name: ")
            if name_in == "stop":
                exit()

        born_date_in: str = input(enter+"Enter birth date\n"
                                  "Example: 01.01.2008: ")
        while not born_date_validator(born_date_in):
            print(error+"Invalid date format. Please enter again.\n"
                        "stop for Exit")
            born_date_in: str = input(re_enter+"Re-Enter birth date\n"
                                      "Example: 01.01.2008: ")
            if born_date_in == "stop":
                exit()

        password_in: str = input(enter+"Enter password: ")
        while len(password_in) < 8:
            print(error+"Password must be at least 8 characters long.\n"
                        "stop for Exit")
            password_in: str = input(re_enter+"Re-Enter password: ")
            if password_in == "stop":
                exit()

        user = User(username=username_in.lower(),
                    name=name_in.capitalize(),
                    born_date=born_date_in,
                    password=password_in)

        data = {
            "username": user.username,
            "name": user.name,
            "born_date": str(user.born_date),
            "password": user.password,
        }
        users = read_all_data("users.json")
        if users == {}:
            users["users"] = [data]
        else:
            users["users"].append(data)
        write_data("users.json", users)
        print(success+"User created successfully.")
        return user


def login():
    """
    Read user data from JSON file and return User object.
    If user not found, return None.
    elif user found, return User dict
    """
    username_in: str = input(enter+"Enter username: ")
    while not username_in:
        print(error+"Username cannot be empty.\n"
                    "stop for Exit")
        username_in: str = input(re_enter+"Re-Enter username: ")
        if username_in == "stop":
            exit()

    users = read_all_data("users.json")

    for user in users["users"]:
        if user["username"] == username_in.lower():
            password_in: str = input(enter+"Enter password: ")
            while len(password_in) < 8:
                print(error+"Password must be at least 8 characters long.\n"
                            "stop for Exit")
                password_in: str = input(re_enter+"Re-Enter password: ")
                if password_in == "stop":
                    exit()

            if user["password"] == password_in:
                user = User(username=username_in.lower(),
                            name=user["name"],
                            born_date=user["born_date"],
                            password=password_in)

                print(success+f"{user.name} logged in successfully.")
                return user
            else:
                print(error+"Incorrect password.")
                return None
    print(error+"User not found.")
    return None


def after_login(user):
    """
    Function to perform actions after successful login
    """
    print(prints+f"Welcome, {user.name}!")

    while True:
        print(command + "1. Edit profile\n"
                        "2. View profile\n"
                        "3. Logout\n")
        choice: str = input(enter + "Enter: ")

        if choice == "1":
            edited_user = get_data(user)
            if edited_user:
                a = read_all_data("users.json")
                dat = {"users": []}
                for user in a["users"]:
                    if user["username"] == user['username']:
                        user["username"] = edited_user.username
                        user["name"] = edited_user.name
                        user["born_date"] = str(edited_user.born_date)
                        user["password"] = edited_user.password
                    dat["users"].append(user)
                print(dat)
                write_data("users.json", dat)

        elif choice == "2":
            print(prints+f"Username: {user.username}\n"
                         f"Name: {user.name}\n"
                         f"Birth Date: {user.born_date}\n"
                         f"Password: {user.password}")

        elif choice == "3":
            print(success+f"{user.name} logged out successfully.")
            return True


def main():
    """
    Main function to run the program
    """

    while True:
        print(command + "1. Create Account\n"
                        "2. Login\n"
                        "3. Exit")
        choice: str = input(enter + "Enter: ")

        if choice == "1":
            user = register()
            if user:
                after_login(user)
                break

        elif choice == "2":
            user = login()
            if user:
                after_login(user)
                break

        elif choice == "3":
            print(success+"Program exited successfully.")
            exit()

        else:
            print(error+"Invalid choice. Please try again.")
