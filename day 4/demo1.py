
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(self.name, "has balance:", self.balance)

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print("Amount must be greater than ZERO")
        else:
            self.balance = self.balance + deposit_amount
            print("Amount Deposited Successfully!")

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Amount must be greater than ZERO")
        elif withdraw_amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - withdraw_amount
            print("Withdrawal Successful!")


# Creating BankAccount object
acc = BankAccount("Thanesh", 50000)

# Display initial balance
acc.show_balance()

print("==============================")

# Deposit operation
deposit_amount = int(input("How much do you want to deposit? "))
acc.deposit(deposit_amount)
acc.show_balance()

print("==============================")

# Withdrawal operation
withdraw_amount = int(input("How much do you want to withdraw? "))
acc.withdraw(withdraw_amount)
acc.show_balance()
