from colorama import Fore, init

init(autoreset=True)

amount_fore = Fore.LIGHTGREEN_EX
withdraw_fore = Fore.LIGHTYELLOW_EX
error_fore = Fore.LIGHTRED_EX
transfer_fore = Fore.LIGHTMAGENTA_EX
success_fore = Fore.LIGHTBLUE_EX
print_fore = Fore.LIGHTCYAN_EX


class Account:
    def __init__(self, name: str, bill: str):
        self.name = name
        self.bill = bill
        self.balance = 0
        self.transfers = []
        print(success_fore+f'Added Account: {bill}!\n')

    def amount(self, amount_of: float):
        self.balance += amount_of
        self.transfers.append(f"+{amount_of}")
        print(amount_fore+f'{amount_of} Added to {self.bill}!\n')

    def withdraw(self, amount_of: float):
        if self.balance >= amount_of:
            self.balance -= amount_of
            self.transfers.append(f"-{amount_of}")
            print(withdraw_fore+f'{amount_of} Withdrawn from {self.bill}!\n')
        else:
            print(error_fore+f'Insufficient funds\nBalance: {self.balance}\n')

    def display(self):
        plus = 0
        minus = 0
        print(print_fore+f"Hisob Raqam: {self.bill}\n    Hisob Egasi: {self.name}")
        for transfer in self.transfers:
            print(print_fore+f"    {transfer}")
            if transfer[:1] == "+":
                plus += int(transfer[1:])
            elif transfer[:1] == "-":
                minus += int(transfer[1:])
        print(amount_fore+f"    Kirim: {plus}")
        print(withdraw_fore+f"    Chiqim: {minus}")
        print(print_fore+f'    Balance: {self.balance}\n')


class Customer:
    def __init__(self, name: str, id_user: str):
        self.name = name
        self.id_user = id_user
        self.balance = 0
        self.accounts = []
        print(success_fore+f'Added Customer {name}!\n')

    def add_account(self, account: Account):
        self.accounts.append(account)
        print(success_fore+f'{account.bill} Added!\n')

    def display(self):
        print(print_fore+f'Name: {self.name}\n    ID: {self.id_user}')
        for account in self.accounts:
            self.balance += account.balance
            print(print_fore+f'    {account.bill} Balance: {account.balance}')
        print(print_fore+f'    Balance of Customer: {self.balance}\n')


class Bank:
    def __init__(self):
        self.balance = 0
        self.customers = []
        print(success_fore+'Added Bank!\n')

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(success_fore+f'{customer.name} Added!\n')

    def transfer(self, account: Account, amount: float, account_to: Account):
        if account.balance >= amount:
            account.withdraw(amount)
            account_to.amount(amount)
            print(transfer_fore+f"{account.bill}-Dan {amount}ming {account_to.bill}-ga O'tqazildi!")
            print(transfer_fore+f'{account.bill}-ni Balansi: {account.balance}\n')

    def display(self):
        print("###########################")
        for customer in self.customers:
            customer.display()
            self.balance += customer.balance
        print(print_fore+f'Balance of Bank: {self.balance}\n')


bank = Bank()

customer1 = Customer("Abdurahim", "H001")
customer2 = Customer("Muhammad", "H002")

account1 = Account(customer1.id_user, 'C001')
account2 = Account(customer1.id_user, 'C002')
account3 = Account(customer2.id_user, 'C003')
account4 = Account(customer2.id_user, 'C004')

bank.add_customer(customer1)
bank.add_customer(customer2)

customer1.add_account(account1)
customer1.add_account(account2)
customer2.add_account(account3)
customer2.add_account(account4)

account1.amount(1000)
account2.amount(2000)
account3.amount(3000)
account4.amount(4000)

account1.withdraw(100)
account2.withdraw(200)
account3.withdraw(300)
account4.withdraw(400)

bank.transfer(account1, 500, account2)
bank.transfer(account2, 600, account3)
bank.transfer(account3, 700, account4)
bank.transfer(account4, 800, account1)

account1.display()
account2.display()
account3.display()
account4.display()

bank.display()
