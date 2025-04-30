import random
import os
from datetime import date
import csv
class BankAccount:
  def __init__(self, initial_balance=0, transactions = {}):
    self.balance = initial_balance
    self.transactions = transactions

  #to get the transaction id and store it in a csv file
  def get_transaction_id(self,type,amount):
    while True:
      transaction_id =  random.randint(100000,999999)
      if transaction_id not in self.transactions:
        self.transactions[transaction_id] = {"date": date.today().strftime("%d-%m-%Y"), "transaction": type, "amount" : amount, "balance": self.balance}
        break
    self.update_csv(transaction_id,self.transactions[transaction_id]["date"], type, amount,self.balance)

  #Return the transactions
  def get_transactions_statement(self):
    return self.transactions

  def deposit(self, amount):
    if amount <= 0:
      return 'Deposit amount must be positive'
    self.balance += amount
    self.get_transaction_id("deposit",amount)
    return f"{amount} has been successfully  deposited into your account"

  def withdraw(self, amount):
    if amount <= 0:
      return 'Withdrawal amount must be positive'
    if amount > self.balance:
      return 'Insufficient funds'
    self.balance -= amount
    self.get_transaction_id("withdraw",amount)
    return f"{amount} has been successfully withdrawn from your account"

  def check_balance(self):
    return f"Current Balance: {self.balance}"
  
  def update_csv(self,id,date,type,amount,balance):
    write_header = not os.path.exists("myaccount.csv") or os.path.getsize("myaccount.csv") == 0
    with open("myaccount.csv","a",newline="") as file:
        writer = csv.writer(file)
        if write_header:
          writer.writerow(["Id","Date","Type","Amount","Balance"])
        writer.writerow([id,date,type,amount,balance])

  def load_from_previous_statements(self):
    write_header = not os.path.exists("myaccount.csv") or os.path.getsize("myaccount.csv") == 0
    if write_header:
          return "Previous transactions not available"
    
    self.transactions = {}
    self.balance = 0
    with open("myaccount.csv","r") as file:
      reader = csv.reader(file)
      next(reader)
      for row in reader:
        if len(row) < 5:
          continue
        transaction_id = int(row[0])
        tran_date = row[1]
        tran_type = row[2]
        tran_amount = int(row[3])
        balance = int(row[4])

        self.transactions[transaction_id] = {"date" : tran_date,
          "transaction" : tran_type,
          "amount" : tran_amount,
          "balance" : balance}
        self.balance = balance
        


my_account = BankAccount()
while True:
  operation = int(input("Please enter the transaction number \n 1. Deposit \n 2. Withdrawl \n 3. Statement \n 4. Check balance \n 5. Include previous transactions \n 6. Exit \n"))
  
  if operation == 1:
    amount = int(input("Please enter the deposit amount \n"))
    print(my_account.deposit(amount))

  elif operation == 2:
    amount = int(input("Please enter withdraw amount \n"))
    print(my_account.withdraw(amount))

  elif operation == 3:
    transactions = my_account.get_transactions_statement()
    print("Transaction ID, Date, Type, Amount, Balance")
    for id, tran in transactions.items():
      print(f'{id},{tran["date"]},{tran["transaction"]},{tran["amount"]},{tran["balance"]}')

  elif operation == 4:
    print(my_account.check_balance())

  elif operation == 5:
    my_account.load_from_previous_statements()

  elif operation == 6:
    break

  else:
    print("Please enter valid key: \n")
