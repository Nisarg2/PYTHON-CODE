amount=int(input("enter a number"))
if amount>10000:
    print("discount=",amount*20/100)
elif amount>7000 and amount<=10000:
    print("discount=",amount*15/100)
elif amount>=7000:
    print("discount=",amount*10/100)
else:
    print("none")