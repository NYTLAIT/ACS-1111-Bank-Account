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
            
    def deposit(self):


    def to_string(self):
        print(f'Name: {self.full_name} Num: {self.account_number} Balance: {self.balance}')


example_account = BankAccount('xamxam1')
example_account2 = BankAccount('xamxam2')

example_account.to_string()
example_account2.to_string()