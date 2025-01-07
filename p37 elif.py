num1=int(input("enter a first number"))
num2=int(input("enter a second number"))
num3=int(input("enter a third number"))
if num1>num2 and num1>num3:
     print("num 1 is greater")
elif num2>num1 and num2>num3:
     print("num 2 is greater")
elif num3>num1 and num3>num2:
     print("num 3 is greater")
else:
     print("all numbers")