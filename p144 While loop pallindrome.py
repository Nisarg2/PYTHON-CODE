no=int(input("enter a number:"))
r=0
z=no
while no>0:
    y =no % 10
    r =(r *10)
    no= no/10
if z==r:
    print("It's pallindrome number")
else:
    print("It's not pallindrome number")
            