import math

no = int(input("enter a number:"))
r = 0
z = no
while no > 0:
    y = no % 10
    r = r+ math.factorial(y)
    no = no // 10
if z == r:
    print("It's Krishanmurti number")
else:
    print("It's not krishanmurti number")