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
        print(f'Balance: ${self.balance}')
        return self.balance
    
    def add_interest(self):
        if self.balance > 0:
            self.balance = self.balance * 1.00083
            print(f'Balance: ${round(self.balance, 2)}')
        else:
            print('Get out of debt first')

    def print_statement(self):
        account_number_hidden = '****' + str(self.account_number)[-4:]
        print(f'{self.full_name}')
        print(f'Account No.: {account_number_hidden}')
        print(f'Balance: ${round(self.balance, 2)}')

# CHECK
example_account = BankAccount('xamxam1')
example_accounttoo = BankAccount('xamxam2')

example_account.deposit(100) # balance 100
example_account.deposit(50) # balance 150

example_account.withdraw(25) # balance 125
example_account.withdraw(5) # balance 120
example_account.withdraw(140) # balance -30

example_account.get_balance() # balance -30

example_account.add_interest() # Get out of debt first
example_account.deposit(80) # balance 50
example_account.add_interest() # balance 50.04

example_account.print_statement()