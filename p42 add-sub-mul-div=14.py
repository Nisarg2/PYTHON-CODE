print("press 1 for Addition")
print("press 2 for Subtraction")
print("press 3 for Multiplication")
print("press 4 for Division")
op=int(input("enter opt =>"))
if op==1:
    no1=int(input("enter a number"))
    no2= int(input("enter a number"))
    print("sum=",no1+no2)
elif op==2:
    no1=int(input("enter a number"))
    no2=int(input("enter a number"))
    print("sum=",no1-no2)

elif op==3:
    no1=int(input("enter a number"))
    no2=int(input("enter a number"))
    print("sum=",sum*sum)

elif op==4:
    no1=int(input("enter a number"))
    no2=int(input("enter a number"))
    print("sum=",no1/no2)
else:
    print("wrong opt")

