import random
cr=0
cz=0
for i in range(1,3):
    no1=random.randint(1,50)
    no2=random.randint(1,50)
    op=random.randint(1,3)
    print("No1 = ",no1," No2 = ",no2)
    if op==1:
        add=int(input("Enter add =>"))
        if add == no1+no2:
            print("right")
            cr=cr+1
        else:
            print("wrong")
            cz=cz+1
    elif op==2:
        sub= int(input("Enter sub=>"))
        if sub == no1 - no2:
            print("right")
            cr = cr + 1
        else:
            print("wrong")
            cz = cz + 1
    elif op==3:
        mul = int(input("Enter mul=>"))
        if sub == no1 - no2:
                print("right")
                cr = cr + 1
        else:
                print("wrong")
                cz = cz + 1
print("right answers:",cr)
print("wrong answers:",cz)