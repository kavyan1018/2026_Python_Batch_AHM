# x = int(input("Enter a number: "))

# match x:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
        
#     case _:
#         print("Invalid input")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = input("Enter operation (+, -, *, /): ")

match sum:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operation")