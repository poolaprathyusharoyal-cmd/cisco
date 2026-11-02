
class BankAccount:

    def __init__(self, name, balance):
        print("Hi This is Constructor....! we are initializing globally at once")

        self.name = name
        self.balance = balance

    def showbalance(self):
        print("Hi This is balance Method Method")
        print(self.name, "has balance", self.balance)


# Creating first object
acc1 = BankAccount("Thanesh", 500000)

# Calling method using object reference
acc1.showbalance()

# We can call the same method multiple times
# acc1.showbalance()
# acc1.showbalance()

print("========================")

# Creating second object
acc2 = BankAccount("Ramesh", 600000)

acc2.showbalance()


# Concept	Meaning
# class	Blueprint for creating objects
# __init__()	Constructor, called automatically when an object is created
# self	Refers to the current object
# acc1, acc2	Objects of BankAccount
# showbalance()	Instance method
# self.name	Object attribute
# self.balance	Object attribute