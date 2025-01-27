no = int(input("enter a number:"))
r = 0
z = no
while no > 0:
    y = no % 10
    r = r+ y*y*y
    no = no // 10

print("R = ",r," Z = ",z)
if z == r:
    print("It's armstrong number")
else:
    print("It's not armstrong number")

#153
# 27
#125
#  1
