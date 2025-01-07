sub1 = int(input("Enter marks for Sub 1: "))
sub2 = int(input("Enter marks for Sub 2: "))
sub3 = int(input("Enter marks for Sub3: "))
total = sub1 + sub2 + sub3
print("total marks=",total)
if total>=100:
    print("grade A")
elif total>=50 and total<100:
    print("grade B")
elif total>100:
    print("grade C")
else:
    print("fail")
