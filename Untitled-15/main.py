# from .database import phone_details, email_details
import os
import csv
from collections import defaultdict
from colorama import Fore, init


init(autoreset=True)

error = Fore.RED
enter = Fore.CYAN
re_enter = Fore.MAGENTA
success = Fore.LIGHTGREEN_EX
prints = Fore.YELLOW

filename = os.path.join(os.getcwd(), 'contact.csv')

email_details = ['@mail.ru', '@gmail.com', '@icloud.com']

phone_details = ['50', '90', '91', '93', '94', '95', '97', '98', '99']


class Users:
    def __init__(self, first_name, last_name, phone, username, password, email):
        self.full_name = f"{first_name} {last_name}"
        self.username = username
        try:
            if len(phone) == 9 and phone.isdigit() and phone[:2] in phone_details:
                self.phone = phone
        except ValueError:
            raise ValueError("Invalid Phone Number!")
        try:
            if len(password) >= 8:
                self.password = password
        except ValueError:
            raise ValueError("Invalid Password!")
        try:
            if email.endswith(tuple(email_details)):
                self.email = email
        except ValueError:
            raise ValueError("Invalid Email Address!")

    def __str__(self):
        return f"{self.full_name}\n{self.username}\n{self.phone}\n{self.password}\n{self.email}"


def postt():
    first_name = 'Abdurahim'
    last_name = 'Egamberdiyev'
    phone = '987654321'
    username = 'egamberdiyev_a'
    password = '12345678'
    email = 'a@gmail.com'

    user = Users(first_name, last_name, phone, username, password, email)
    print(user)


postt()