
class Employee:

    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def show_employee(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

    def update_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary must be greater than ZERO")

        self.salary = salary
        print("Salary Updated Successfully!")

    def increase_salary(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than ZERO")

        self.salary = self.salary + amount
        print("Salary Increased Successfully!")


emp = Employee(101, "Thanesh", 50000)

while True:

    print("\n====== EMPLOYEE MENU ======")
    print("1. Show Employee")
    print("2. Update Salary")
    print("3. Increase Salary")
    print("4. Exit")
    print("===========================")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank You!")
        break

    try:
        if choice == "1":
            emp.show_employee()

        elif choice == "2":
            salary = float(input("Enter New Salary: "))
            emp.update_salary(salary)

        elif choice == "3":
            amount = float(input("Enter Increase Amount: "))
            emp.increase_salary(amount)

        else:
            raise ValueError("Invalid Menu Choice!")

    except ValueError as error:
        print("Error:", error)

    except Exception as error:
        print("Unexpected Error:", error)

    else:
        print("Operation Completed Successfully!")

    finally:
        print("Employee Operation Attempt Completed!")
