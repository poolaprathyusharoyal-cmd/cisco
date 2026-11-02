
try:
    n1 = int(input("Enter A value : "))
    n2 = int(input("Enter B value : "))

    result = n1 / n2

except ValueError as error:
    print("Please Enter the Number only...!")

except ZeroDivisionError as error:
    print("Boss we cannot divide anything zero : please enter positive number")

except TypeError as error:
    print("Cannot add number and string")
    print(error)

except IndexError:
    print("Index does not exist!")

except KeyError:
    print("Key does not exist!")

except NameError:
    print("Variable is not defined!")

except FileNotFoundError:
    print("File does not exist!")

except AttributeError:
    print("String does not support append()")

else:
    print("Sum of A / B : ", result)

finally:
    print("CALCULATION COMPLETED, Thank you ...!")
