class Account:
    def __init__(self,name,pin,balance=0):
        self.name=name
        self.pin=pin
        self.balance=balance

class ATM:
    def __init__(self,account):
        self.account=account
        self.access_granted= False
        self.transactions= []

    def verify_pin(self,entered_pin):
        if entered_pin == self.account.pin:
            self.access_granted = True
        else:
            return 'Incorrect pin'

    def deposit(self,amount):
        if self.access_granted:
            self.account.balance += amount
            self.transactions.append(f'+{amount}')
            return 'Transaction successful'

    def withdraw(self,amount):
        if self.access_granted:
            if amount > self.account.balance:
                return 'Insufficient funds'
            else:
                self.account.balance -= amount
                self.transactions.append(f'-{amount}')
                return 'Transaction successful'

    def check_balance(self):
        if self.access_granted:
            return f'Your balance is {self.account.balance}'


my_card=Account('mason',1234,0)
b = ATM(my_card)
print(b.verify_pin(1234))
print(b.deposit(500))
print(b.withdraw(200))
print(b.check_balance())
print(b.transactions)

