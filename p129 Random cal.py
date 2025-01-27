import random
print("press 1 for Addition")
print("press 2 for Subtraction")
print("press 3 for Multiplication")
print("press 4 for Division")
opt=int(input("enter opt =>"))
cr=0
cz=0
for i in range(1,6):
    if opt==1:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if a+b==c:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz= cz + 1

    elif opt==2:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if a-b==c:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz = cz + 1
    elif opt==3:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if a*b==c:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz = cz + 1
    elif opt==4:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if a/b==c:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz = cz + 1

    else:
        print("wrong opt")
        cz = cz + 1
import random
print("press 1 for Addition")
print("press 2 for Subtraction")
print("press 3 for Multiplication")
print("press 4 for Division")
opt=int(input("enter opt =>"))
cr=0
cz=0
for i in range(1,3):
    if opt==1:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if c==a+b:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz= cz + 1

    elif opt==2:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if c==a-b:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz = cz + 1
    elif opt==3:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if c==a*b:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz = cz + 1
    elif opt==4:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print("No1=", a, "No2", b)
        c = int(input("Enter ans =>"))
        if c==a/b:
            print("right ans",cr)
            cr=cr+1
        else:
            print("wrong ans",cz)
            cz = cz + 1
    else:
        print("wrong opt")
print("\ntotal right ans=", cr)
print("\ntotal wrong ans=",cz)