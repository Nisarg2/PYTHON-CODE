print("press 1 for area of triangle")
print("press 2 for area of circle")
op=int(input("enter opt =>"))
if op==1:
    height=int(input("enter a height"))
    base=int(input("enter a base"))
    print("area of triangle=",0.5*height*base)
elif op==2:
    radius=int(input("enter a radius"))
    print("area of circle=", 3.14*radius*radius)
else:
    print("wrong opt")