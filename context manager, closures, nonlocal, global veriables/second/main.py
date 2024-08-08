import json
import os

from colorama import Fore, init


init(autoreset=True)

error = Fore.RED
enter = Fore.CYAN
re_enter = Fore.MAGENTA
success = Fore.LIGHTGREEN_EX
prints = Fore.YELLOW
command = Fore.LIGHTCYAN_EX

path = f"{os.path.dirname(os.path.abspath(__file__))}/"


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
    lis = {}
    count_id = 0
    with CustomOpen(file_path, "r") as file:
        ls = json.load(file)
        for x in ls["orders"]:
            counter = 0
            if lis.get("orders"):
                for i in lis["orders"]:
                    if (x["user"] == i["user"] and
                            x["total_price"] == i["total_price"] and
                            x["products"] == i["products"]):
                        counter += 1
                if counter == 0:
                    count_id += 1
                    x['id'] = count_id
                    lis["orders"].append(x)
            else:
                x['id'] = 1
                count_id += 1
                lis["orders"] = [x]
    return write_data(filename, lis)


def write_data(filename, data):
    file_path = path + filename
    """
    Write data to JSON file
    """
    with CustomOpen(file_path, "w") as file:
        json.dump(data, file, indent=4)
        return True


def main():
    filename = "orders.json"
    while True:
        print(command + "1. Fix Orders\n"
                        "2. Exit\n"
                        "I have a dublicate(dubl.json) json file for more testing.")
        choice: str = input(enter + "Enter: ")
        if choice == "1":
            read_all_data(filename)
            print(success + "Orders fixed successfully.")

        elif choice == "2":
            break

        else:
            print(error + "Invalid input, please try again.")

