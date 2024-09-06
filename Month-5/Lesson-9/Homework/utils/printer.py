from colorama import Fore, init

init(autoreset=True)

success = Fore.LIGHTGREEN_EX


def user_printer(dat):
    print(success + f"{dat['id']} | {dat['first_name']} | {dat['last_name']} | {dat['email']} | {dat['password']} | "
                    f"{dat['date_of_birth']} | {dat['gender']} | {dat['role']} | {dat['company_id']} | {dat['salary']} | {dat['created_at']}")


def company_printer(dat):
    print(success + f"{dat['id']} | {dat['name']} | {dat['created_at']}")


def department_printer(dat):
    print(success + f"{dat['id']} | {dat['name']} | {dat['company_id']} | {dat['created_at']}")
