
# Creating a dictionary
employee = {
    "name": "Thanesh",
    "age": 25,
    "Salary": 50000
}

# 1. Print complete dictionary
print("========== EMPLOYEE DETAILS ==========")
print(employee)

# 2. Access a particular value
print("\n========== ACCESS VALUE ==========")
print("Employee Name:", employee["name"])
print("Employee Age:", employee["age"])
print("Employee Salary:", employee["Salary"])

# 3. Update an existing value
print("\n========== UPDATE AGE ==========")
employee.update({"age": 26})
print(employee)

# 4. Add a new key-value pair
print("\n========== ADD DESIGNATION ==========")
employee.update({"Designation": "Manager"})
print(employee)

# 5. Display all keys
print("\n========== KEYS ==========")
print(employee.keys())

# 6. Display all values
print("\n========== VALUES ==========")
print(employee.values())

# 7. Display all key-value pairs
print("\n========== ITEMS ==========")
print(employee.items())

# 8. Access value using get()
print("\n========== GET METHOD ==========")
print(employee.get("name"))
print(employee.get("Salary"))

# 9. Remove a particular key using pop()
print("\n========== POP METHOD ==========")
employee.pop("age")
print(employee)

# 10. Create a copy of dictionary
print("\n========== COPY METHOD ==========")
employee_copy = employee.copy()
print(employee_copy)

# 11. Check whether a key exists
print("\n========== CHECK KEY ==========")
if "name" in employee:
    print("Name key exists")
else:
    print("Name key does not exist")

# 12. Display number of items
print("\n========== LENGTH ==========")
print("Total items:", len(employee))

# 13. Remove all dictionary elements
print("\n========== CLEAR METHOD ==========")
employee.clear()
print(employee)
