# Bank account system
# Class: BankAccount
# Attributes: owner_name, balance, account_nukmber
# Methods: deposit(), withdraw(), check_balance()

class BankAccount:
    def __init__(self, owner, balance=0, pin="1234"):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if self.verify_pin(pin):
            self._balance += amount
            print(f"{self.owner} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid PIN. Deposit failed.")

    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                print(f"{self.owner} withdraw ${amount}. New balance: ${self._balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid PIN. Withdrawal failed.")

    def check_balance(self):
        print(f"{self.owner} has ${self._balance}")

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Amount must be positive.")

    def verify_pin(self, pin):
        return self.__pin == pin

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
            print(f"{index} - {account.owner} has ${account._balance}")
    elif menu == "2":
        owner = input("Enter account owner name: ")
        balance = float(input("Enter initial balance: "))
        pin = input("Enter account PIN: ")
        new_account = BankAccount(owner, balance, pin)
        accounts.append(new_account)
        print(f"Account created for {owner} with balance ${balance}")
    elif menu == "3":
        index = int(input("Enter account index: "))
        amount = float(input("Enter deposit amount: "))
        pin = input("Enter account PIN: ")
        accounts[index].deposit(amount, pin)
    elif menu == "4":
        index = int(input("Enter account index: "))
        amount = float(input("Enter withdrawal amount: "))
        pin = input("Enter account PIN: ")
        accounts[index].withdraw(amount, pin)
    elif menu == "5":
        break
    else:
        print("Invalid menu option. Please try again.")