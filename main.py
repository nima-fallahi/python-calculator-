print(" Welcome to python Calculator,"
      " Your calculator, simplified. ")
result = None
while True:
    choice = input(
        "1. Mathematical Operations - 2. Unit Conversion - 3. Exit: ")
    if choice == "1":
        print("Mathematical Operations")
        num1 = int(input("first number : "))
        num2 = int(input("second number : "))
        result = None
        operation = input(" +, -, *, /, ")
        if operation == "+":
            result = num1 + num2
            print("Addition", result)
        elif operation == "-":
            result = num1 - num2
            print("Subtraction", result)
        elif operation == "*":
            result = num1 * num2
            print("Multiplication", result)
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print("Division:", result)
            else:
                result = None
                print("Cannot divide by zero")
    elif choice == "2":
        if result is None:
            number = float(input("Enter a number : "))
        else:
            number = result
        operation = input(
            "1. CM to MM - 2. M to CM - 3. KG to G - 4. G to KG:")
        print("Your number is:", number)
        print("Your conversion:", operation)

        if operation == "1":
            print("Result:", number * 10)
        elif operation == "2":
            print("Result:", number * 100)
        elif operation == "3":
            print("Result:", number * 1000)
        elif operation == "4":
            print("Result:", number / 1000)
        else:
            print("Invalid conversion")
    elif choice == "3":
        break
    else:
        print("Invaild choice")
print(" Thank you for your using python Calculator. keep learning, keep building! ")
