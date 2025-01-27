no=int(input("enter no =>"))
z=0
while no>0:
    x=no%10
    z=z*10+x
    no=no//10
print("Reverse no = ",z)


