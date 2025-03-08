class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def display_details(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    withdrawal_limit = 500
    
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal limit exceeded! Max allowed: ${self.withdrawal_limit}")
        else:
            super().withdraw(amount)


class PremiumSavingsAccount(SavingsAccount):
    withdrawal_limit = 2000


accounts = []

def create_account():
    acc_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    acc_type = input("Enter account type (basic/savings/premium): ").lower()
    
    if acc_type == "savings":
        new_account = SavingsAccount(acc_number, balance)
    elif acc_type == "premium":
        new_account = PremiumSavingsAccount(acc_number, balance)
    else:
        new_account = BankAccount(acc_number, balance)
    
    accounts.append(new_account)
    print("Account created successfully!")

def list_accounts():
    for index, account in enumerate(accounts):
        print(f"{index} - Account Number: {account.account_number}, Balance: ${account.balance}")

def deposit():
    index = int(input("Enter account index: "))
    amount = float(input("Enter deposit amount: "))
    if 0 <= index < len(accounts):
        accounts[index].deposit(amount)
    else:
        print("Invalid account index.")

def withdraw():
    index = int(input("Enter account index: "))
    amount = float(input("Enter withdrawal amount: "))
    if 0 <= index < len(accounts):
        accounts[index].withdraw(amount)
    else:
        print("Invalid account index.")

def display_account():
    index = int(input("Enter account index: "))
    if 0 <= index < len(accounts):
        accounts[index].display_details()
    else:
        print("Invalid account index.")

while True:
    print("\n__Menu__")
    print("1. List accounts")
    print("2. Create account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Display account details")
    print("6. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        list_accounts()
    elif menu == "2":
        create_account()
    elif menu == "3":
        deposit()
    elif menu == "4":
        withdraw()
    elif menu == "5":
        display_account()
    elif menu == "6":
        break
    else:
        print("Invalid menu option. Please try again.")