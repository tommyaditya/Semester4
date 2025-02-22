# Bank account system
# Class: BankAccount
# Attributes: owner_name, balance, account_nukmber
# Methods: deposit(), withdraw(), check_balance()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"{self.owner} has ${self.balance}")

accounts = []

while True:
    print("__Menu__")
    print("1. List accounts")
    print("2. Create account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        for index, account in enumerate(accounts):
            print(f"{index} - {account.owner} has ${account.balance}")
    elif menu == "2":
        owner = input("Enter account owner name: ")
        balance = float(input("Enter initial balance: "))
        new_account = BankAccount(owner, balance)
        accounts.append(new_account)
        print(f"Account created for {owner} with balance ${balance}")
    elif menu == "3":
        index = int(input("Enter account index: "))
        amount = float(input("Enter deposit amount: "))
        accounts[index].deposit(amount)
    elif menu == "4":
        index = int(input("Enter account index: "))
        amount = float(input("Enter withdrawal amount: "))
        accounts[index].withdraw(amount)
    elif menu == "5":
        break
    else:
        print("Invalid menu option. Please try again.")