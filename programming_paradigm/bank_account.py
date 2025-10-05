class BankAccount:
    """A simple bank account class that supports deposits, withdrawals, and balance display."""

    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount from the balance if sufficient funds exist.
        Return True if successful, otherwise False.
        """
        if amount > self.account_balance:
            return False  # Insufficient funds
        else:
            self.account_balance -= amount
            return True  # Withdrawal successful

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance}")
