class BankAccount:
    def __init__(self, starting_balance=0):
        self.account_balance = starting_balance

    def deposit(self, amount):
        self.account_balance += amount
        

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"The current account balance is {self.account_balance}")
