age=int(input("enter a age"))
if age>0 and age<=12:
    print("a child")
elif age>12 and age<19:
    print("a teenager")
elif age>20 and age<64:
    print("a adult")
elif age<65:
    print("a senior")
else:
    print("no")