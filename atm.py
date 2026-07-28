wallet = 5000.00
attempts = 3
balance_history = []

while True:
    code = input("TO ACCESS YOUR ACCOUNT PLEASE ENTER YOUR 4-DIGIT CODE: ")
    if len(code) != 4:
        print("MUST BE A 4 DIGIT CODE! STOP PLAYING W ME!!")
    else:
        code = int(code)
    if code == 1234:
        print("WELCOME. HOW CAN WE ASSIST YOU TODAY?!")
        break
    else:
        attempts -= 1
        print(f"INCORRECT CODE! YOU HAVE  {attempts} ATTEMPTS REMAINING!!")

        if attempts == 0:
         print("BLOCKED! TRY AGAIN LATER")
         exit()

while True:
    print("---WELCOME,HOW CAN I ASSIST YOU TODAY?---")
    menu = input("1. Check Balance, 2. Deposit, 3. Withdraw, 4.Balance History:")
    if menu == "1":
        print(f"Your current balance is R{wallet:.2f}")
        print("THANK YOU FOR USING OUR BANK,GOODBYE.")

    elif menu == "2":
            deposit = float(input("Enter the amount you would like to deposit:"))
            wallet += deposit
            balance_history.append(deposit)
            print("TRANSACTION SUCCESSFUL")
            print(f"Your new balance is R{wallet:.2f}.")
            print("THANK YOU FOR USING OUR BANK,GOODBYE.")


    elif menu == "3":
            withdraw_amt = float(input("How much would you like to withdraw?: "))
            if withdraw_amt > wallet:
                print("INSUFFICIENT FUNDS!")
            else:
                wallet -= withdraw_amt
                print("TRANSACTION SUCCESSFUL")
                balance_history.append(-withdraw_amt)
                print(f"Your new balance is R{wallet:.2f}.")
                print("THANK YOU FOR USING OUR BANK,GOODBYE.")


    elif menu == "5":
        print("THANK YOU FOR USING OUR BANK,GOODBYE.")
    exit()
