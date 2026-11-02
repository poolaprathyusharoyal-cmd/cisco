# Keyword                  Purpose

# try                     Contains code that may cause an exception
# except                  Handles an exception
# else                    Executes when no exception occurs
# finally                 Executes whether an exception occurs or not
# raise                   Manually raises an exception



age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("You are eligible")