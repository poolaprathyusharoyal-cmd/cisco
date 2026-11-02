
class EmployeeManagement:

    def __init__(self):
        self.employees = set()

    # 1. Add Employee
    def add_employee(self):
        try:
            empid = int(input("Enter Employee ID: "))

            if empid <= 0:
                raise ValueError("Employee ID must be positive")

            name = input("Enter Employee Name: ").strip()

            if not name:
                raise ValueError("Employee name cannot be empty")

            salary = float(input("Enter Employee Salary: "))

            if salary <= 0:
                raise ValueError("Salary must be positive")

            # Check duplicate employee ID
            for emp in self.employees:
                if emp[0] == empid:
                    raise ValueError("Employee ID already exists")

            employee = (empid, name, salary)

            self.employees.add(employee)

        except ValueError as e:
            print("Invalid input:", e)

        else:
            print("Employee added successfully!")

        finally:
            print("Add operation completed.")

    # 2. View Employees
    def view_employees(self):
        try:
            if not self.employees:
                raise ValueError("No employee records found")

            print("\nEmployee Details:")

            for emp in sorted(self.employees):
                print("ID:", emp[0])
                print("Name:", emp[1])
                print("Salary:", emp[2])
                print("--------------------")

        except ValueError as e:
            print("Error:", e)

        finally:
            print("View operation completed.")

    # 3. Search Employee
    def search_employee(self):
        try:
            empid = int(input("Enter Employee ID to search: "))

            for emp in self.employees:
                if emp[0] == empid:
                    print("\nEmployee Found!")
                    print("ID:", emp[0])
                    print("Name:", emp[1])
                    print("Salary:", emp[2])
                    break
            else:
                raise ValueError("Employee not found")

        except ValueError as e:
            print("Error:", e)

        finally:
            print("Search operation completed.")

    # 4. Update Salary
    def update_salary(self):
        try:
            empid = int(input("Enter Employee ID: "))

            for emp in self.employees:
                if emp[0] == empid:

                    salary = float(input("Enter New Salary: "))

                    if salary <= 0:
                        raise ValueError("Salary must be positive")

                    # Remove old tuple
                    self.employees.remove(emp)

                    # Add updated tuple
                    updated_employee = (emp[0], emp[1], salary)
                    self.employees.add(updated_employee)

                    print("Salary updated successfully!")
                    break
            else:
                raise ValueError("Employee not found")

        except ValueError as e:
            print("Error:", e)

        finally:
            print("Update operation completed.")

    # 5. Delete Employee
    def delete_employee(self):
        try:
            empid = int(input("Enter Employee ID to delete: "))

            for emp in self.employees:
                if emp[0] == empid:
                    self.employees.remove(emp)
                    print("Employee deleted successfully!")
                    break
            else:
                raise ValueError("Employee not found")

        except ValueError as e:
            print("Error:", e)

        finally:
            print("Delete operation completed.")

    # 6. Display Employee IDs using Set
    def view_employee_ids(self):
        ids = {emp[0] for emp in self.employees}
        print("Employee IDs:", ids)


# Create object
obj = EmployeeManagement()

# Main Menu
while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. View Employee IDs")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.add_employee()

        elif choice == 2:
            obj.view_employees()

        elif choice == 3:
            obj.search_employee()

        elif choice == 4:
            obj.update_salary()

        elif choice == 5:
            obj.delete_employee()

        elif choice == 6:
            obj.view_employee_ids()

        elif choice == 7:
            print("Exiting Employee Management System...")
            break

        else:
            print("Invalid choice! Select 1 to 7.")

    except ValueError:
        print("Please enter a valid menu number.")

    finally:
        print("Menu operation completed.")
