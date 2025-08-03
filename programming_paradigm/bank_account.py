class BankAccount:
    def __init__(self):
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds")
            return False

    def display_balance(self):
        print(f"The current account balance is {self.account_balance}")
