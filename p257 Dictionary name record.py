students = {12: "ram", 25: "jayul", 35: "rahul", 41: "ami", 55: "riya", 45: "hiral", 33: "karan"}
c=0
name=(input("Enter a Name=>"))
for k, v, in students.items():
    if v == name:
        print( "\t", k)
        c = 1
        break

if c == 0:
    print("not found")
