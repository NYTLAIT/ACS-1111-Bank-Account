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
        print(f'Amount deposited: ${amount} New Balance: ${round(self.balance, 2)}')

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= amount
            self.balance -= 10
            print(f'Insufficient funds. Incured $10 overdraft fee')
            print(f'Balance: {round(self.balance, 2)}')
        else: 
            self.balance -= amount
            print(f'Amount deposited: ${amount} New Balance: ${round(self.balance, 2)}')

    def get_balance(self):
        print(f'Balance: ${round(self.balance, 2)}')
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

john_smith = BankAccount('John Smith')
scarlett_johansson = BankAccount('Scarlett Johansson')
jane_eyre = BankAccount('Jane Eyre')


john_smith.deposit(100)
john_smith.withdraw(120)
scarlett_johansson.deposit(200)
scarlett_johansson.get_balance()
jane_eyre.deposit(300)
jane_eyre.add_interest

mitchell_dudson = BankAccount('Mitchell Dudson')
mitchell_dudson.deposit(400000)
mitchell_dudson.print_statement()
mitchell_dudson.add_interest()
mitchell_dudson.print_statement()
mitchell_dudson.withdraw(150)
mitchell_dudson.print_statement()