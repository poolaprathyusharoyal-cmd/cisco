
while True:
    try:
        n1 = int(input("Enter A Value: "))
        n2 = int(input("Enter B Value: "))

        result = n1 / n2

    except ValueError:
        print("Please enter numbers only! Try again.")

    except ZeroDivisionError:
        print("Cannot divide by ZERO! Try again.")

    else:
        print("Division Result:", result)
        break

    finally:
        print("Calculation attempt completed!")
