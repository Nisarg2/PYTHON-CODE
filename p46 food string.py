print("press P for panipuri")
print("press p for pizza")
print("press b for bhel")
print("press s for sandwich")
op=input("enter opt =>").lower()
if op=="P":
    print("Price of Panipuri 30")
    qty=int(input("Enter qty =>"))
    print("Bill of panipuri = ",qty*30)
elif op=="p":
    print("price of pizza 160")
    qty=int(input("enter a qty"))
    print("bill of pizza=",qty*160)
elif op=="b":
    print("price of bhel 100")
    qty=int(input("enter a qty =>"))
    print("bill of bhel=",qty*100)
elif op=="s":
    print("price of sandwich 150")
    qty=int(input("enter a qty"))
    print("bill of sandwich=",qty*150)
else:
    print("wrong opt")

