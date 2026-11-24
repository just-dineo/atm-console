import json

class DebitCard:
    def __init__(self,bank):
        self.bank = bank

    def pay(self,entered_pin,amount):
        if self.bank.withdraw(entered_pin,amount):
           return True
        else:
            return False
class ATM:
    def __init__(self,bank):
        self.bank=bank

    def withdraw(self,entered_pin,amount):
       if self.bank.withdraw(entered_pin,amount):
         return f'TRANSACTION SUCCESSFUL\nYOUR BALANCE IS NOW: {self.bank.check_balance(entered_pin)}'
       else:
           return 'INCORRECT PIN'

    def deposit(self,entered_pin,amount):
        if self.bank.deposit(entered_pin,amount):
            return f'TRANSACTION SUCCESSFUL\nYOUR BALANCE IS NOW: {self.bank.check_balance(entered_pin)}'
        else:
            return 'INCORRECT PIN'

    def check_balance(self,entered_pin):
        if self.bank.check_balance(entered_pin):
            return f'{self.bank.check_balance(entered_pin)}'
        else:
            return 'INCORRECT PIN'

    def info(self,entered_pin):
        if self.bank.info(entered_pin):
            return f'{self.bank.info(entered_pin)}'
        else:
            return 'INCORRECT PIN'
    def transaction_history(self,entered_pin):
        history= self.bank.transaction_history(entered_pin)
        if history is not False:
            return f'{self.bank.transaction_history(entered_pin)}'
        else:
            return 'INCORRECT PIN'

class BankDatabase:
    def load_data(self):
       with open("accounts.json","r") as file:
           data=json.load(file)
       return data

    def save_data(self,info):
        with open("accounts.json","w") as file:
            json.dump(info,file,indent=2)

class Bank:
    def __init__(self,database,bank_name='PYTHON BANK'):
        self.database=database
        self.bank_name=bank_name

    def withdraw(self,entered_pin,amount):
        data=self.database.load_data()
        for customer in data["customers"]:
            if entered_pin == customer["pin"]:
               if amount > customer["wallet"]:
                 raise Exception("insufficient funds")
               else:
                customer["wallet"] -= amount
                customer["transactions"].append(f'-{amount}')
                self.database.save_data(data)
                return True
        return False

    def deposit(self,entered_pin,amount):
        data = self.database.load_data()
        for customer in data["customers"]:
            if entered_pin == customer["pin"]:
               if amount <= 0:
                raise Exception("insufficient amount")
               else:
                customer["wallet"] += amount
                customer["transactions"].append(f'+{amount}')
                self.database.save_data(data)
                return True
        return False
    def transaction_history(self,entered_pin):
        data = self.database.load_data()
        for customer in data["customers"]:
            if entered_pin == customer["pin"]:
               return customer["transactions"]
        return False

    def check_balance(self,entered_pin):
        data = self.database.load_data()
        for customer in data["customers"]:
            if entered_pin == customer["pin"]:
              return f'YOUR BALANCE IS {customer["wallet"]}'
        return False

    def info(self,entered_pin):
        data = self.database.load_data()
        for customer in data["customers"]:
            if entered_pin == customer["pin"]:
              return f'{self.bank_name}\nName: {customer["name"]}\nAccount Number: {customer["account number"]}\nBalance: {customer["wallet"]}'
        return False


def main():
    db=BankDatabase()
    my_bank=Bank(db)
    atm=ATM(my_bank)
    my_card=DebitCard(my_bank)
    print(atm.withdraw(432,100))
    print(atm.deposit(1234,6000))
    print(my_card.pay(2222,1000))
    print(atm.check_balance(4321))
    print(atm.info(2222))
    print(atm.deposit(4321,2000.03))
    print(atm.transaction_history(2222))
    print(my_card.pay(2222,100))
    print(atm.transaction_history(4321))
    print(my_card.pay(1234,200.50))
    print(atm.check_balance(1234))
    print(atm.info(1111))
    print(atm.transaction_history(1111))

if __name__ == "__main__":
    main()

