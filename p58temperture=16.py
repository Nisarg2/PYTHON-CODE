temp=int(input("enter a temp number"))
if temp<0:
    print("fezzing atmosphere")
elif temp<10:
    print("very cold atmosphere")
elif temp<20:
    print("cold atmosphere")
elif temp<30:
    print("normal atmosphere")
elif temp<40:
    print("hot atmosphere")
elif temp>40:
    print("very hoy atmosphere")
else:
    print("other")