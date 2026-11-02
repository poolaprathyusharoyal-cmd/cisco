
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(self.name, "has balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than ZERO")
        else:
            self.balance = self.balance + amount
            print("Amount Deposited Successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than ZERO")
        elif amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - amount
            print("Withdrawal Successful!")


# Creating Bank Account Object
acc = BankAccount("Thanesh", 50000)

# Banking Menu
while True:

    print("\n========== BANK MENU ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("===============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc.show_balance()

    elif choice == "2":
        amount = int(input("Enter Deposit Amount: "))
        acc.deposit(amount)
        acc.show_balance()

    elif choice == "3":
        amount = int(input("Enter Withdraw Amount: "))
        acc.withdraw(amount)
        acc.show_balance()

    elif choice == "4":
        print("Thank you for Banking!")
        break

    else:
        print("Invalid Choice! Try Again.")
