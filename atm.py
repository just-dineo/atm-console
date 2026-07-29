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



while True:
    print("HELLO. HOW CAN WE HELP YOU TODAY?")
    print()
    action=input("1. CHECK BALANCE. 2. DEPOSIT 3. WITHDRAW 4.EXIT: " )

    if action== "1":
        name=input("PLEASE ENTER YOUR FULL NAME: ").lower()
        if name in accounts:
            code=int(input("PLEASE ENTER YOUR 4- CODE: "))

            if code == accounts[name]["pin"]:
                print(f"WELCOME {name.upper()}")
                print(f"YOUR BALANCE IS R{accounts[name]['wallet']:.2f}")

            else:
                  print("INCORRECT CODE")
        else:
          print("ACCOUNT NOT FOUND!")
        break

    elif action == "2":
        name = input("PLEASE ENTER YOUR FULL NAME: ").lower()
        if name in accounts:
          code = int(input("PLEASE ENTER YOUR 4- CODE: "))

          if code == accounts[name]["pin"]:
            print(f"WELCOME {name.upper()}")
            deposit=int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?: "))

            if deposit <= 0:
                print("ENTER A VALID AMOUNT!!")

            else:
                accounts[name]["wallet"] += deposit
                print("TRANSACTION SUCCESSFUL")
                print(f"YOUR BALANCE IS R{accounts[name]['wallet']:.2f}")
                print("THANK YOU FOR USING OUR BANK, GOODBYE!")
                break
          else:
            print("INCORRECT CODE")
        else:
         print("ACCOUNT NOT FOUND!")


    elif action == "3":
       name = input("PLEASE ENTER YOUR FULL NAME: ").lower()
       if name in accounts:
        code = int(input("PLEASE ENTER YOUR 4- CODE: "))

        if code == accounts[name]["pin"]:
            print(f"WELCOME {name.upper()}")
            amt=int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW?: "))

            if amt > accounts[name]['wallet']:
                    print("INSUFFICIENT FUNDS")
            else:
              accounts[name]['wallet'] -= amt
              print("TRANSACTION SUCCESSFUL")
              print(f"YOUR BALANCE IS R{accounts[name]['wallet']}")
              print("THANK YOU FOR USING OUR BANK, GOODBYE!")
              break

        else:
               print("INCORRECT CODE!")

       else:
            print("ACCOUNT NOT FOUND!")
    elif action == "4":
        print("THANK YOU FOR USING OUR BANK.GOODBYE!")
        break

