print("press 1 for panipuri")
print("press 2 for pizza")
print("press 3 for bhel")
print("press 4 for sandwich")
op=int(input("enter opt"))
if op==1:
    print("Price of Panipuri 30")
    qty=int(input("Enter qty =>"))
    print("Bill of panipuri = ",qty*30)
elif op==2:
    print("price of pizza 160")
    qty=int(input("enter a qty"))
    print("bill of pizza=",qty*160)
elif op==3:
    print("price of bhel 100")
    qty=int(input("enter a qty"))
    print("bill of bhel=",qty*100)
elif op==4:
    print("price of sandwich 150")
    qty=int(input("enter a qty"))
    print("bill of sandwich=",qty*150)
else:
    print("wrong opt")

