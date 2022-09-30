"""
Type hinting exercise
"""


def main():
    """Simple program for illustrative purposes"""
    age: int = ask_user_age()
    print_age(age)

def ask_user_age():
    """Return user input"""
    age: int = input("What is your age in years? ")
    return int(age)


def print_age(age):
    """Print full sentence"""
    age_in_months: int = age * 12
    print(f"You are {age_in_months} months old.")


if __name__ == "__main__":
    main()


