try:
    a = int(input("Enter the value for a: "))
    b= int(input("Enter the value for b : "))
    
    print("What operation do you want to perform.\nPress + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division\n")
    o = input("Enter operation : ")
    match o:
        case "+":
            print(f"The addition of a and b is : {a + b}")
        case "-":
            print(f"The subtraction of a and b is : {a - b}")
        case "*":
            print(f"The multiplication of a and b is :{a*b}")
        case "/":
            if b==0:
                print("The value for b can never be zero")
            else:
                print(f"The division of a and b is :{a / b}")
        case default:
            print("There was an error")
except Exception as e:
    print("Enter a valid inputs for a and b ")
ch = input("do you want to continue? (y/n): ")
if ch.lower() != 'y':
