from abc  import ABC
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
    
# interface
class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass

class CreditAction(Enum):
        DEPOSIT  = 0
        WITHDRAW = 1

class CreditCardCommand(Command):
    def __init__(self, account, action, amount):
        self.account = account
        self.action  = action
        self.amount  = amount
        self.success = None
     
    def invoke(self):
        if self.action == CreditAction.DEPOSIT:
            self.success = self.account.deposit(self.amount)
        elif self.action == CreditAction.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
    
    def undo(self):
        if not self.success:
            return
        if self.action == CreditAction.DEPOSIT:
            self.account.withdraw(self.amount)
        if self.action == CreditAction.WITHDRAW:
            self.account.deposit(self.amount)
    

if __name__ == '__main__':
    card = CreditCard()
    cmd  = CreditCardCommand(card, CreditAction.DEPOSIT, 100)
    cmd.invoke()
    print('     - card balance =', card.balance)
    cmd.undo()
    print('     - card balance =', card.balance)
    cmd = CreditCardCommand(card, CreditAction.WITHDRAW, 1000)
    cmd.invoke()
    print('     - (illegal withdrawal card balance =', card.balance)
    cmd.undo()
    print('     - card balance =', card.balance)

