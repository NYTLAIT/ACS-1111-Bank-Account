import random

class BankAccount:
    registered_accounts_num = []

    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = self.account_num_randomizer()
        self.balance = 0

    def account_num_randomizer(self):
        while True:
            count = 0
            number = ''
            while count < 8:
                count += 1
                number += str(random.randint(0, 9))

            if number not in self.registered_accounts_num:
                self.registered_accounts_num.append(number)
                return int(number)
            
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} New Balance: ${self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= amount
            self.balance -= 10
            print(f'Insufficient funds. Incured $10 overdraft fee')
            print(f'Balance: {self.balance}')
        else: 
            self.balance -= amount
            print(f'Amount deposited: ${amount} New Balance: ${self.balance}')

    def get_balance(self):
        print(f'Balance: {self.balance}')
        return self.balance

    def to_string(self):
        print(f'Name: {self.full_name} Num: {self.account_number} Balance: {self.balance}')

# CHECK
example_account = BankAccount('xamxam1')
example_accounttoo = BankAccount('xamxam2')

example_account.to_string()
example_accounttoo.to_string()

example_account.deposit(100) # balance 100
example_account.deposit(50) # balance 150

example_account.withdraw(25) # balance 125
example_account.withdraw(5) # balance 120
example_account.withdraw(140) # balance -30

example_account.get_balance()