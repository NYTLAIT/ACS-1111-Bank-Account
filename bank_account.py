import random

class BankAccount:
    registered_accounts_num = []

    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = self.account_num_randomizer()
        self.balance = 0

    def account_num_randomizer(self):
        '''
        Generate a unique 8 digit numeric string. 
        '''
        # Create 8 digit number by looping through a random number from 0-9 using random.randint
        # and adding them together while a count gets added by 1 each loop -- loop stops when 
        # count is 8. checks if 8 digit number has been used. If not, will add the number to a
        # list of used numbers and return the number.
        while True:
            count = 0
            number = ''
            while count < 8:
                count += 1
                number += str(random.randint(0, 9))

            if number not in self.registered_accounts_num:
                self.registered_accounts_num.append(number)
                return number
            
    def deposit(self, amount):
        '''
        Add an amount to BankAccount object balance and display amount and new balance.
        
        :param amount: Deposit amount -- amount added to balance
        :type amount: int
        '''
        self.balance += amount
        print(f'Amount deposited: ${amount} New Balance: ${round(self.balance, 2)}')

    def withdraw(self, amount):
        '''
        Subtract an amount to BankAccount object balance and display amount and new balance.
        If amount more than object balance, subtract additional 10 to simulate overdraft fee
        and display alert of overdraft for insufficient funds.
        
        :param amount: Withdraw amount -- amount subtracted from balance
        :type amount: int
        '''
        if amount > self.balance:
            self.balance -= amount
            self.balance -= 10
            print(f'Insufficient funds. Inccured $10 overdraft fee')
            print(f'Balance: {round(self.balance, 2)}')
        else: 
            self.balance -= amount
            print(f'Amount deposited: ${amount} New Balance: ${round(self.balance, 2)}')

    def get_balance(self):
        '''
        Print BankAccount object balance and return balance.

        :return balance: BankAccount object balance
        '''
        print(f'Balance: ${round(self.balance, 2)}')
        return self.balance
    
    def add_interest(self):
        '''
        Add interest of 0.83% to BankAccount object balance if balance is greater than 0
        and print new balance. If not greater, print alert of insufficient funds. 
        '''
        if self.balance > 0:
            self.balance = self.balance * 1.00083
            print(f'Balance: ${round(self.balance, 2)}')
        else:
            print('Get out of debt first')

    def print_statement(self):
        '''
        Print BankAccount object full name, hidden bank account number showing only last 4 digits,
        and balance rounded to 2 decimal points.
        '''
        account_number_hidden = '****' + self.account_number[-4:]
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