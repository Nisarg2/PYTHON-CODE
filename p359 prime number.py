no=int(input("Enter number =>"))
c=1

for i in range(2,no):
    if no % i ==0:
        c=0
        break

if c==0:
    print("No is not prime")
else:
    print("No is prime")