import random
cr=0
cz=0
for i in range(1,6):
    a=random.randint(1,50)
    b=random.randint(1,50)
    print("No1 = ",a," No2 = ",b)
    c=int(input("Enter add =>"))
    if a+b==c:
        print("right ans")
        cr=cr+1
    else:
        print("wrong ans")
        cz=cz+1

print("\ntotal right ans=",cr)
print("\ntotal wrong ans=",cz)