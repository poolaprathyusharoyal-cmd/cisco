
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(self.name, "has balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than ZERO")
        else:
            self.balance += amount
            print("Amount Deposited Successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than ZERO")
        elif amount > self.balance:
            raise ValueError("Insufficient Funds!")
        else:
            self.balance -= amount
            print("Withdrawal Successful!")


acc = BankAccount("Thanesh", 50000)

while True:

    print("\n========== BANK MENU ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("===============================")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you for Banking!")
        break

    try:
        if choice == "1":
            acc.show_balance()

        elif choice == "2":
            amount = int(input("Enter Deposit Amount: "))
            acc.deposit(amount)

        elif choice == "3":
            amount = int(input("Enter Withdraw Amount: "))
            acc.withdraw(amount)

        else:
            raise ValueError("Invalid Menu Choice!")

    except ValueError as error:
        print("Error:", error)

    except Exception as error:
        print("Unexpected Error:", error)

    else:
        print("Operation Completed Successfully!")

    finally:
        print("Bank Transaction Attempt Completed!")
