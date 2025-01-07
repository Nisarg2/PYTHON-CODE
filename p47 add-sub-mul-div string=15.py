print("press + for Addition")
print("press - for Subtraction")
print("press * for Multiplication")
print("press / for Division")
op=input("enter opt =>")
if op=="+":
    no1=int(input("enter a number"))
    no2= int(input("enter a number"))
    print("sum=",no1+no2)
elif op=="-":
    no1=int(input("enter a number"))
    no2=int(input("enter a number"))
    print("sum=",no1-no2)

elif op=="*":
    no1=int(input("enter a number"))
    no2=int(input("enter a number"))
    print("sum=",sum*sum)

elif op=="/":
    no1=int(input("enter a number"))
    no2=int(input("enter a number"))
    print("sum=",no1/no2)
else:
    print("wrong opt")

