x =  int(input("Enter a number: "))


match x:
    case 1:
        print("You Selected Gujarati")
        print("1..Roti")
        print("2..Dal")
        print("3..Rice")
        print("4..Sabji")
        print("5..Dessert")
        ch = int(input("Enter a char : "))

        match ch:
            case 1:
                print("1..plain roti")
                print("2..Bhakri")
                print("3..Rotlo")
                
                roti = int(input("Enter a number: "))
                print("You Selected ", roti)
                
                print("How Much do u want ?")
                qu = (int(input("Enter number : ")))
                qu = qu * 12
                
                print("Total bill = ",qu)
                
                
    case 2:
        print("You Selected Punjabi")
    case 3:
        print("You Selected Rajasthani")