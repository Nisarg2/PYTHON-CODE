while True:
    print("opt 1 for squre")
    print("opt 2 for cube")
    print("opt 3 for exit")
    opt=int(input("enter a opt"))
    if opt==1:
         n=int(input("enter a number"))
         print("squre",n*n)
    elif opt==2:
        n=int(input("enter a number"))
        print("cube",n*n*n)
    elif opt==3:
        print("bye")
        break
    else:
        print("wrong opt")