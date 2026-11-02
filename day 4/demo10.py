
class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        try:
            empid = int(input("Enter Employee ID: "))

            if empid <= 0:
                raise ValueError("Employee ID must be positive")

            for emp in self.employees:
                if emp["id"] == empid:
                    raise ValueError("Employee ID already exists")

            name = input("Enter Employee Name: ")

            if not name.strip():
                raise ValueError("Employee name cannot be empty")

            salary = float(input("Enter Employee Salary: "))

            if salary <= 0:
                raise ValueError("Salary must be positive")

            employee = {
                "id": empid,
                "name": name,
                "salary": salary
            }

            self.employees.append(employee)

        except ValueError as e:
            print("Invalid input:", e)

        except Exception as e:
            print("Error:", e)

        else:
            print("Employee added successfully!")

        finally:
            print("Add employee operation completed.")

    def view_employees(self):
        try:
            if not self.employees:
                raise ValueError("No employee records found")

            print("\nEmployee Details:")
            for emp in self.employees:
                print("ID:", emp["id"])
                print("Name:", emp["name"])
                print("Salary:", emp["salary"])
                print("--------------------")

        except ValueError as e:
            print(e)

        finally:
            print("View operation completed.")

    def search_employee(self):
        try:
            empid = int(input("Enter Employee ID to search: "))

            for emp in self.employees:
                if emp["id"] == empid:
                    print("\nEmployee Found!")
                    print("ID:", emp["id"])
                    print("Name:", emp["name"])
                    print("Salary:", emp["salary"])
                    break
            else:
                raise ValueError("Employee not found")

        except ValueError as e:
            print("Error:", e)

        finally:
            print("Search operation completed.")

    def update_salary(self):
        try:
            empid = int(input("Enter Employee ID: "))

            for emp in self.employees:
                if emp["id"] == empid:
                    salary = float(input("Enter New Salary: "))

                    if salary <= 0:
                        raise ValueError("Salary must be positive")

                    emp["salary"] = salary
                    print("Salary updated successfully!")
                    break
            else:
                raise ValueError("Employee not found")

        except ValueError as e:
            print("Error:", e)

        finally:
            print("Update operation completed.")

    def delete_employee(self):
        try:
            empid = int(input("Enter Employee ID to delete: "))

            for emp in self.employees:
                if emp["id"] == empid:
                    self.employees.remove(emp)
                    print("Employee deleted successfully!")
                    break
            else:
                raise ValueError("Employee not found")

        except ValueError as e:
            print("Error:", e)

        finally:
            print("Delete operation completed.")


obj = EmployeeManagement()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

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
            print("Exiting Employee Management System...")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")

    except ValueError:
        print("Please enter a valid number.")

    finally:
        print("Menu operation completed.")
