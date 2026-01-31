import math
# Simple Calculator

while True:
    print("--- Python Console Calculator ---")
    print("Select operation: +, -, *, /, %, //, sqrt, **, quit, or !")

    # 1. Take user input for the operation
    operation = input("Enter operation: ")

    if operation == 'quit':
        print("Exiting the calculator. Goodbye!")
        break

    # 2. Take user input for numbers (converted to floats)
    num1 = float(input("Enter first number: "))    

    # Lab 5 adding factorial operation
    if operation == '!':
        total = 1 # i.e. 1 * 2 * 3 ... * x
        if num1 < 0 or not num1.is_integer():
            print("Error: Factorial is only defined for non-negative integers.")
        else:
            for i in range(2, int(num1) + 1):
                total *= i
        print(f'{int(num1)}! = {total}')
        continue

    elif operation == 'sqrt':
        result = math.sqrt(num1)
        print(f"math.sqrt({num1}) = {result}")
        continue

    num2 = float(input("Enter second number: "))

    # 3. Perform the calculation based on the operation
    # conditiional operation
    if operation == '+': # note ==
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    # read this as else if
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == '**':
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")

    elif operation == '%':
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")

    elif operation == '//':
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")

    elif operation == '/':
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero.")          
    # handle no match case
    else:
        print("Invalid operation selected.")
