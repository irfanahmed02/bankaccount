import bankaccount

user = bankaccount.UsersManagement()
user.load_users_from_csv()
while True:
    user_input = input("Please select the below: \n [C]reate account \n [S]ign in \n [E]xit \n").lower()

    if user_input == "c":
        print(user.create_account())

    elif user_input == "s":
        username = user.signin()
        if not username:
            continue
        else:
            user_account = bankaccount.BankAccount(username)
            user_account.load_from_csv()
            while True:

                operation = input("Please enter the transaction number \n [D]eposit \n [W]ithdrawal \n [S]tatement \n Check [B]alance \n [E]xit \n").lower()
                
                if operation == "d":
                    try:
                        amount = float(input("Please enter the deposit amount \n"))
                        print(user_account.deposit(amount))
                    except ValueError:
                        print("Please enter the valid number")

                elif operation == "w":
                    try:
                        amount = float(input("Please enter withdraw amount \n"))
                        print(user_account.withdraw(amount))
                    except ValueError:
                        print("Please enter the valid number")

                elif operation == "s":

                    transactions = user_account.get_statement()
                    print("Transaction ID, Date, Type, Amount, Balance")
                    for id, tran in transactions.items():
                        print(f'{id},{tran["date"]},{tran["type"]},{tran["amount"]},{tran["balance"]}')

                elif operation == "b":
                    print(user_account.check_balance())

                elif operation == "e":
                    break

                else:
                    print("Please enter valid key: \n")

    elif user_input == "e":
        break

    else:
        print("Please enter valid key \n")