num=(int(input("enter the number==>")))

if num%2!=0:
    print("Weird")

elif num%2==0:
    if num>2 and num<5:
        print("not wierd")
    elif num>6 and num<20:
        print("Weird")
    elif num>20:
        print("not Weird")

else:
    print("not found")