import bankaccount

user = bankaccount.UsersManagement()
user.load_users_from_csv()
while True:
    user_input = input("Please select the below: \n 1. Create account \n 2. Sign in \n 3. Exit \n")

    if user_input == "1":
        print(user.create_account())

    elif user_input == "2":
        username = user.signin()
        if not username:
            continue
        else:
            user_account = bankaccount.BankAccount(username)
            user_account.load_from_csv()
            while True:

                operation = input("Please enter the transaction number \n 1. Deposit \n 2. Withdrawal \n 3. Statement \n 4. Check balance \n 5. Exit \n")
                
                if operation == "1":
                    try:
                        amount = float(input("Please enter the deposit amount \n"))
                        print(user_account.deposit(amount))
                    except ValueError:
                        print("Please enter the valid number")

                elif operation == "2":
                    try:
                        amount = float(input("Please enter withdraw amount \n"))
                        print(user_account.withdraw(amount))
                    except ValueError:
                        print("Please enter the valid number")

                elif operation == "3":

                    transactions = user_account.get_statement()
                    print("Transaction ID, Date, Type, Amount, Balance")
                    for id, tran in transactions.items():
                        print(f'{id},{tran["date"]},{tran["type"]},{tran["amount"]},{tran["balance"]}')

                elif operation == "4":
                    print(user_account.check_balance())

                elif operation == "5":
                    break

                else:
                    print("Please enter valid key: \n")

    elif user_input == "3":
        break

    else:
        print("Please enter valid key")