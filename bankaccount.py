import random
class BankAccount:
  def __init__(self, initial_balance=0, transactions = {}):
    self.balance = initial_balance
    self.transactions = transactions

  #to get the transaction id and store it in a dictionary
  def get_transaction_id(self,type,amount):
    while True:
      transaction_id =  random.randint(100000,999999)
      if transaction_id not in self.transactions:
        self.transactions[transaction_id] = {"transaction": type, "amount" : amount}
        break

  #Return the transactions
  def get_transactions_statement(self):
    return self.transactions

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount
    self.get_transaction_id("deposit",amount)
    return f"{amount} has been successfully  deposited into your account"

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount
    self.get_transaction_id("withdraw",amount)
    return f"{amount} has been successfully credit from your account"

  def check_balance(self):
    return f"Current Balance: {self.balance}"
  


  


  