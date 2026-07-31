accounts=  {"eleanor smith" : { "pin": 1234,
                           "wallet": 5000.00
                            },
        "john bull": { "pin": 2345,
                       "wallet": 5000.00
                       },
        "mason blue": { "pin": 4768,
                        "wallet": 5000.00
                        }
        }

transaction_history= []

running= True
while True:

print("HELLO. HOW CAN WE HELP YOU TODAY.")
name=input("PLEASE ENTER YOUR NAME: ")
if name in accounts:
    code=int(input("ENTER YOUR 4 DIGIT CODE: "))
    if code == accounts[name]['pin']:
        print(f"WELCOME {name}")

        active_session= True
        while active_session:
            option = input("1.CHECK BALANCE 2.WITHDRAW 3.DEPOSIT 4.TRANSACTION HISTORY 5.EXIT: ")
            if option == "1":
                print(f"YOUR BALANCE IS: R{accounts[name]['wallet']}")
            elif option == "2":
                amt=float(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW: "))
                if amt > accounts[name]['wallet']:
                    print("INSUFFICIENT FUNDS!")
                else:
                    accounts[name]['wallet'] -= amt
                    print(f"TRANSACTION SUCCESSFUL! YOUR BALANCE IS :{accounts[name]['wallet']}")
                    transaction_history.append(f"WITHDREW: {amt}")
            elif option == "3":
                deposit=float(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?: "))
                if deposit <=0:
                    print("ENTER A VALID AMOUNT!")
                else:
                    accounts[name]['wallet'] += deposit
                    transaction_history.append(f"DEPOSITED: {deposit}")
                    print(f"TRANSACTION SUCCESSFUL! YOUR BALANCE IS NOW: R{accounts[name]['wallet']}")
            elif option == "4":
                slip=input("WOULD YOU LIKE TO VIEW YOUR TRANSACTION HISTORY?(Y OR N): ").lower()
                if slip == "y":
                    print("--------RECEIPT--------")
                    print(transaction_history)
                    print("-----------------------")
                else:
                    print("TIMEOUT")
            elif option == "5":
                print("THANK YOU FOR USING OUR BANK.GOODBYE")
                active_session=False
                running=False
                break
        if not running:
            break
    else:
        print("INCORRECT PIN")
else:
    print("ACCOUNT NOT FOUND")

