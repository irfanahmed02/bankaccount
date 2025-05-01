import os
from datetime import date
import csv
import hashlib

class UsersManagement:
   
      def __init__(self,users = None):
          self.users = users if users else {}
        
      #Hashing password
      def hash_password(self,password):
         return hashlib.sha256(password.encode()).hexdigest()

      def load_users_from_csv(self):
          if not os.path.exists("users.csv"):
             return
          with open("users.csv","r") as file:
             reader = csv.reader(file)
             next(reader)
             for row in reader:
                if len(row) == 2:
                  user = row[0]
                  password = row[1]
                  self.users[user] = password                
      
      def create_account(self):
          while True:
            new_username = input("Please enter username: (or press e for exit) \n")
            if new_username == "e":
              return "Exit"
            if new_username in self.users:
              print("username not available")
              continue
            pw = self.hash_password(input("Create new password \n"))
            pw2 = self.hash_password(input("Reenter the password \n"))
            if pw != pw2:
                print("Password doesnt match \n")
                continue
            self.users[new_username] = pw
            write_header = not os.path.exists("users.csv") or os.path.getsize("users.csv") == 0
            with open("users.csv","a",newline="") as file:
               
               writer = csv.writer(file)
               if write_header:
                  writer.writerow(["Username", "Password"])
               writer.writerow([new_username, pw])
                  
               
            return "Account has been created"
          
      def signin(self):
          while True:
            username = input("Please enter username: (or press e to Exit) \n")
            if username == "e":
              break
            password = self.hash_password(input("please enter password \n"))
            if username not in self.users or self.users[username] != password:
              print("username or password is incorrect")
              continue
            else:
              print("Access Granted")
              return username
          

class BankAccount:

    def __init__(self,username, initial_balance=0, transactions = None):
      self.username= username
      self.balance = initial_balance
      self.transactions = transactions if transactions else {}
      self.last_transaction_id = max(self.transactions.keys(), default=100000)
      

    #to get the transaction id and store it in a csv file
    def get_transaction_id(self,type,amount):
      self.last_transaction_id += 1
      self.transactions[self.last_transaction_id] = {"date": date.today().strftime("%d-%m-%Y"), "type": type, "amount" : amount, "balance": self.balance}
      self.update_csv(self.last_transaction_id,self.transactions[self.last_transaction_id]["date"], type, amount,self.balance)

    #Printing the statement
    def get_statement(self):
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
      write_header = not os.path.exists(f"{self.username}.csv") or os.path.getsize(f"{self.username}.csv") == 0
      with open(f"{self.username}.csv","a",newline="") as file:
          writer = csv.writer(file)
          if write_header:
            writer.writerow(["Id","Date","Type","Amount","Balance"])
          writer.writerow([id,date,type,amount,balance])

    def load_from_csv(self):
      write_header = not os.path.exists(f"{self.username}.csv") or os.path.getsize(f"{self.username}.csv") == 0
      if write_header:
        return "Welcome, we are excited for your first transaction!"
      
      
      self.transactions = {}
      self.balance = 0
      with open(f"{self.username}.csv","r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
          if len(row) < 5:
            continue
          transaction_id = int(row[0])
          tran_date = row[1]
          tran_type = row[2]
          tran_amount = float(row[3])
          balance = float(row[4])

          self.transactions[transaction_id] = {"date" : tran_date,
            "type" : tran_type,
            "amount" : tran_amount,
            "balance" : balance}
          self.balance = balance
      self.last_transaction_id = max(self.transactions.keys(), default=100000)
      return "Welcome Back!"
