first_number = int(input())
second_number = int(input())
operation = input()
if (operation == "/" or operation == "%") and second_number == 0:
    print(f"Cannot divide {first_number} by zero")
else:
    if operation == "+" or operation == "-" or operation == "*":
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        if result % 2 == 0:
            type_number = "even"
        else:
            type_number = "odd"
        print(f"{first_number} {operation} {second_number} = {result} - {type_number}")
    elif operation == "/":
        result = first_number / second_number
        print(f"{first_number} {operation} {second_number} = {result:.2f}")
    elif operation == "%":
        result = first_number % second_number
        print(f"{first_number} {operation} {second_number} = {result}")
