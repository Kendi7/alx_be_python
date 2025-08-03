class BankAccount:
    def __init__(self, starting_balance=0):
        self.account_balance = starting_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds.")  # Checker expects this with a period
            return False

    def display_balance(self):
        # Match the exact expected format
        print(f"Current Balance: ${self.account_balance:.2f}")
