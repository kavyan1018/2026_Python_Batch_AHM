x = int(input("Enter a number: "))

match x:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
        
    case _:
        print("Invalid input")