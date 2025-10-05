class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.account_balance:
            return False
        else:
        self.account_balance -= amount
        return f"Withdrew: ${amount}"

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
