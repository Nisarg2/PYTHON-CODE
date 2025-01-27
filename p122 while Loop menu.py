grand_total=0
while True:
    print("press 1 for panipuri")
    print("press 2 for pizza")
    print("press 3 for manchurian")
    print("press 4 for sandwich")
    print("press 5 for exit")
    op=int(input("enter opt"))
    if op==1:
        print("Price of Panipuri 30")
        qty=int(input("Enter qty =>"))
        cost=30*qty
        print("Bill of panipuri = ",qty*30)
        grand_total+=cost
    elif op==2:
        print("price of pizza 160")
        qty=int(input("enter a qty"))
        cost=160*qty
        print("bill of pizza=",qty*160)
        grand_total += cost
    elif op==3:
        print("price of manchurian 100")
        qty=int(input("enter a qty"))
        cost=100*qty
        print("bill of manchurian=",qty*100)
        grand_total += cost
    elif op==4:
        print("price of sandwich 150")
        qty=int(input("enter a qty"))
        cost=150*qty
        print("bill of sandwich=",qty*150)
        grand_total += cost
    elif op==5:
        print("grand_total=",grand_total)
        print("bye")
        break
    else:
        print("wrong opt")

