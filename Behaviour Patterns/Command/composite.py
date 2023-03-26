# Also an example of the composite design pattern.

import unittest
from abc import ABC, abstractmethod
from enum import Enum

class CreditCard:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}')
        return True
    
    def withdraw(self, amount):
        if self.balance - amount >= CreditCard.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, balance = {self.balance}')
            return True
        print('Insufficient funds.')
        return False

    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass


class CreditCardCommand(Command):
    def __init__(self, account, action, amount):
        super().__init__()
        self.account = account
        self.action  = action
        self.amount  = amount

    class Action(Enum):
        DEPOSIT  = 0
        WITHDRAW = 1

    def invoke(self):
        if self.action   == self.Action.DEPOSIT:
            self.success =  self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success =  self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:  self.account.withdraw(self.amount)
        if self.action == self.Action.WITHDRAW: self.account.deposit(self.amount)
    

class CompositeCreditCardCommand(Command, list):
    """Illustration as a composite design pattern."""
    def __init__(self, items:list[Command]=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()
    
    def undo(self):
        for x in reversed(self):
            x.undo()
    
class MoneyTransferCommand(CompositeCreditCardCommand):
    def __init__(self, from_acc, to_acc, amount):
        super().__init__([
            CreditCardCommand(from_acc, CreditCardCommand.Action.WITHDRAW, amount),
            CreditCardCommand(to_acc,   CreditCardCommand.Action.DEPOSIT,  amount)
        ])
    
    def invoke(self):
        """
        pass state ok=self.success
        MACRO: sequence of commands
        """
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok

class TestSuite(unittest.TestCase):
    def test_composit_deposit(self):
        card = CreditCard()
        print(card)
        dep1 = CreditCardCommand(card, CreditCardCommand.Action.DEPOSIT, 1000)
        dep2 = CreditCardCommand(card, CreditCardCommand.Action.DEPOSIT, 1000)
        comp = CompositeCreditCardCommand([dep1, dep2])
        comp.invoke()
        print(card)
        comp.undo()
        print(card)
    
    def test_transfer_fail(self):
        """
        self.successs is not adequately passed in this solution.
        The dependency between the two commands needs to be made explicit.
        """
        card  = CreditCard(100)
        card2 = CreditCard()
        amt   = 1000
        wc    = CreditCardCommand(card,  CreditCardCommand.Action.WITHDRAW, amt)
        dc    = CreditCardCommand(card2, CreditCardCommand.Action.DEPOSIT,  amt)
        trns  = CompositeCreditCardCommand([wc, dc])
        trns.invoke()
        print(f'card: {card}, card2: {card2}')
        trns.undo()
        print(f'card: {card}, card2: {card2}')


    def test_better_transfer(self):
        crd1 = CreditCard(100)
        crd2 = CreditCard()
        mnt  = MoneyTransferCommand(
            from_acc = crd1,
            to_acc   = crd2,
            amount   = 1000)
        mnt.invoke()
        print(f'crd1: {crd1}, crd2: {crd2}')
        mnt.undo()
        print(f'crd1: {crd1}, crd2: {crd2}')
        print('mnt.success: ', mnt.success)
    
if __name__ == '__main__':
    unittest.main()