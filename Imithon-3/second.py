

class BankAccount:
    def __init__(self, account_number: int, owner: str, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        self.transactions = []
    
    def deposit(self, amount: int, account):
        if account.__balance >= amount:
            self.__balance += amount
            self.transactions.append(f'Deposited: ${amount} from {account.owner}')
            self.withdraw(amount)
            print(f'Deposited: ${amount} from {account.owner}')
        else:
            print('Balance Yetmaydi.')
    
    def withdraw(self, amount: int):
        if self.__balance >= amount:
            self.__balance -= amount
            self.transactions.append(f'Withdrew: ${amount}')
            print(f'Withdrew: ${amount}')
        else:
            print('Balance yetmaydi.')
    
    @property
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance: int):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print('Balance must be positive.')
    
    @property
    def get_transactions(self):
        for x in self.transactions:
            print(x)


def main():
    acc1 = BankAccount(86001204, 'Abdurahim', 10000)
    acc2 = BankAccount(86001205, 'Vasiliy', 20000)

    acc1.deposit(5000, acc2)

    acc2.withdraw(3000)

    print(acc1.get_balance)

    acc1.get_transactions