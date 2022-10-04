"""
Type hinting exercise with classes
"""


def main() -> None:
    """Simple program for illustrative purposes"""
    name = ask_name()
    my_account = BankAccount(name)
    my_account.deposit(10000)
    my_account.withdraw(5000)
    my_account.print_balance()


def ask_name():
    """Return user input"""
    name: str = input("What is your name? ")
    return name


class BankAccount:
    """Simple class for bank accounts"""

    def __init__(self, owner):
        """Initialise account (balance 0)"""
        self.owner: str = owner
        self.balance: float = 0

    def deposit(self, amount: float) -> float:
        """Add money to the account"""
        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """Withdraw money from the account"""
        self.balance -= amount

    def print_balance(self):
        """Prints full sentence"""
        print(f"Your account has €{self.balance:,}")

        # Exercise 5
    def my_sum(self, numbers: List[int]):
        total: int = 0
        for n in numbers:
            total += n
        return total


if __name__ == "__main__":
    main()
