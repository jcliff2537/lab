from account import *
from pytest import *


class Test:

    def setup_method(self):
        self.p1 = Account('Jackie')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'Jackie'
        assert self.p1.get_balance() == 0


    def test_deposit(self):
        assert self.p1.deposit(-10) is False
        assert self.p1.get_balance == 0

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance == 0

        assert self.p1.deposit(10) is True
        assert self.p1.get_balance == 10

        assert self.p1.deposit(20.5) is True
        assert self.p1.get_balance == approx(30.5,abs=.001)

        #assert self.p1.deposit(-10) is False
        #assert self.p1.get_balance == approx(30.5,abs=.001)

    def test_withdraw(self):
        assert self.p1.withdraw(10) is False
        assert self.p1.get_balance == 0

        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance == 0

        self.p1.deposit(50)

        assert self.p1.withdraw(10.5) is True
        assert self.p1.get_balance == approx(39.5,abs=.001)

        assert self.p1.withdraw(-10) is False
        assert self.p1.get_balance == approx(39.5,abs=.001)

    """
     make a deposit calling the function self.p1.deposit(30) then
     make a witdrawal (10.5)
    """
