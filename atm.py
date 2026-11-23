class DebitCard:

    def __init__(self, name, number, balance=0, pin=1234, bank='PYTHON BANK'):
        self.name = name
        self.number = number
        self.pin = pin
        self.balance = balance
        self.bank = bank
        self.authorisation = False

    def verify_pin(self, entered_pin):
        if entered_pin != self.pin:
            raise Exception('INCORRECT PIN')
        else:
            self.authorisation = True

    def pay(self, amount):
        if not self.authorisation:
            return ' '
        else:
            self.balance -= amount

    def __str__(self):
        if not self.authorisation:
            return ' '
        else:
            return (
                f'{self.bank}\nName: {self.name}\nAccount number:'
                f' XXXX{self.number[-4:]}\nBalance: {self.balance}'
            )

    def __repr__(self):
        return str(self)


class ATM:

    def __init__(self, card):
        self.card = card
        self.transactions = []

    def verify_login(self, entered_pin):
        self.card.verify_pin(entered_pin)
        if self.card.authorisation:
            return f'WELCOME {self.card.name}'

    def check_balance(self):
        if not self.card.authorisation:
            return ' '
        else:
            return f'YOUR BALANCE IS: {self.card.balance}'

    def deposit(self, amount):
        if not self.card.authorisation:
            return ' '
        else:
            self.card.balance += amount
            self.transactions.append(f'+{amount}')
            return f'TRANSACTION SUCCESSFUL\nYOUR BALANCE IS: {self.card.balance}'

    def withdraw(self, amount):
        if not self.card.authorisation:
            return ' '
        if amount <= self.card.balance:
            self.card.balance -= amount
            self.transactions.append(f'-{amount}')
            return (
                f'TRANSACTION SUCCESSFUL!\nYOUR BALANCE {self.card.balance}'
            )
        else:
            return f'TRANSACTION DECLINED.INSUFFICIENT FUNDS'

    def transaction_history(self):
        return self.transactions


my_card = DebitCard('lenny', '12345678', balance=10000)
print(my_card.verify_pin(1234))
print(my_card.balance)
a = ATM(my_card)
print(a.verify_login(1234))
print(a.check_balance())
print(a.deposit(2000))
print(a.withdraw(1000))
print(a.transactions)
