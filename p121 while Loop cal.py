while True:
    print("press 1 for Addition")
    print("press 2 for Subtraction")
    print("press 3 for Multiplication")
    print("press 4 for Division")
    print("press 5 for exit")
    opt=int(input("enter opt =>"))
    if opt==1:
        no1= int(input("enter a number"))
        no2= int(input("enter a number"))
        print("addition=",no1+no2)
    elif opt==2:
        no1 = int(input("enter a number"))
        no2 = int(input("enter a number"))
        print("subtractions=",no1-no2)
    elif opt==3:
        no1 = int(input("enter a number"))
        no2 = int(input("enter a number"))
        print("multiplication=",no1*no2)
    elif opt==4:
        no1 = int(input("enter a number"))
        no2 = int(input("enter a number"))
        print("division",no1/no2)
    elif opt==5:
        print("bye")
        break
    else:
        print("wrong opt")