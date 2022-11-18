class Account:

        def __init__(self, name):
            account_name = name
            account_balance = 0

        def deposit(self, amount):
            if amount <= 0:
                return False
            else:
                account_balance += amount
                return False

        def withdraw(self, amount):
            if amount <= 0 or amount > account_balance:
                    return False
                else:
                    account_balance -= amount
                    return True
            else:
                return False

        def get_balance(self):
            return account_balance

        def get_name(self):
            return account_name

