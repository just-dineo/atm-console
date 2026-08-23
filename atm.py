accounts = {"eleanor smith": {"pin": 1234,
                               "wallet": 5000.00
                                },
            "john bull": {"pin": 2345,
                           "wallet": 5000.00
                           },
            "mason blue": {"pin": 4768,
                            "wallet": 5000.00
                            }
            }

transaction_history = []
attempts = 3
name_attempts = 3

def main():
    global attempts
    global name_attempts

    def check_balance(balance):
        amt = (f"YOUR BALANCE IS: R{balance}")
        return amt

    while True:
        name_ok = True
        while name_ok:
            print("hello. how can we help you today.")
            name = input("please enter you full name: ")
            if name in accounts:
                pin_ok = True
                while pin_ok:
                    try:
                        code = int(input("please enter you 4-digit code:"))
                    except ValueError:
                        print("please enter numbers only")
                        continue

                    if code == accounts[name]["pin"]:

                        print(f"welcome {name}")

                        active_session = True
                        while active_session:
                            option = input("1.CHECK BALANCE 2.WITHDRAW 3.DEPOSIT 4.TRANSACTION HISTORY 5.EXIT: ")
                            if option == "1":

                                my_balance = check_balance(accounts[name]['wallet'])
                                print(my_balance)
                            elif option == "2":
                                amt = float(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW: "))
                                if amt > accounts[name]['wallet']:
                                    print("INSUFFICIENT FUNDS!")
                                else:
                                    accounts[name]['wallet'] -= amt
                                    print(f"TRANSACTION SUCCESSFUL! YOUR BALANCE IS :{accounts[name]['wallet']}")
                                    transaction_history.append(f"WITHDREW: {amt}")
                            elif option == "3":
                                deposit = float(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?: "))
                                if deposit <= 0:
                                    print("ENTER A VALID AMOUNT!")
                                else:
                                    accounts[name]['wallet'] += deposit
                                    transaction_history.append(f"DEPOSITED: {deposit}")
                                    print(f"TRANSACTION SUCCESSFUL! YOUR BALANCE IS NOW: R{accounts[name]['wallet']}")
                            elif option == "4":
                                slip = input("WOULD YOU LIKE TO VIEW YOUR TRANSACTION HISTORY?(Y OR N): ").lower()
                                if slip == "y":
                                    print("--------RECEIPT--------")
                                    print(transaction_history)
                                    print("-----------------------")
                                else:
                                    print("TIMEOUT")
                            elif option == "5":
                                print("THANK YOU FOR USING OUR BANK.GOODBYE")
                                exit()
                    else:
                        attempts -= 1
                        print(f"incorrect code! you have {attempts} remaining")
                        if attempts == 0:
                            print("blocked. try again later")
                            exit()
            else:
                name_attempts -= 1
                print(f"account not found. try again. you have {name_attempts} remaining")
                if name_attempts == 0:
                    print("account does not exist.try again later!")
                    exit()

if __name__ == '__main__':
    main()
