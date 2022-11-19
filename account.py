class Account:

    def __init__(self, name: str) -> None:
        """
        Function to create objects with account name and balance
        :param name: name of the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to add money to account balance
        :param amount: numeric value for the amount to be deposited
        :return: True if money is added, False if not
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to subtract money from account balance
        :param amount: numeric value for the amount to be withdrawn
        :return: True if money is withdrawn, False if not
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Function to return the current account balance
        :return: returns a numeric value
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to return the name of the account
        :return: returns the account name
        """
        return self.__account_name
