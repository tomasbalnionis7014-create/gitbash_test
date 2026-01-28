# creating the variables that the user will enter


while True:
    print("shalom shalom welcome to the calculator")
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number: "))
    function = input("Enter the operation (+, -, *, /): ")
# performing the calculations based on the user's input
    if function == "+" or function.lower() == "add":
        t = number_one+number_two
        print(f" the result is: {t}")
    elif function == "-" or function.lower() == "subtract":
        result = number_one-number_two
        print(f"the result is: {result}")
    elif function == "*" or function.lower() == "multiply":
        result = number_one*number_two
        print(f" the result is: {result}")
    elif function == "/" or function.lower() == "divide":
        result = number_one/number_two
        print(f"the result is: {result}")
    else:
        print("thats and invalid operation")
    y = input("do you want to perform another calculation? (yes/no): ")
    if y.lower() == "no" or y.lower() == "n":
        print("okay in a bit gang")
        break
