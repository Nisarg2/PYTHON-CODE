import random
for i in range(1,6):
    a=random.randint(1,50)
    b=random.randint(1,50)
    print("No1 = ",a," No2 = ",b)
    c=int(input("Enter add =>"))
    if a+b==c:
        print("right ans")
    else:
        print("wrong ans")