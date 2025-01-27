sub1 = int(input("Enter marks for Sub 1: "))
sub2 = int(input("Enter marks for Sub 2: "))
sub3 = int(input("Enter marks for Sub3: "))
total = sub1 + sub2 + sub3
print("Total Marks=", total)
if total > 50:
    print("Pass")
else:
    print("Fail")
