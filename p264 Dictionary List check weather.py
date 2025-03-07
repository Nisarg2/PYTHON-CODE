marks={"ram": 33,"rahul": 45,"devesh": 30,"jayul": 34,"meena": 29,"nisha": 37,"karan": 40,"anita": 18,"siddhi": 25}
name=input("enter your sweet name=>")
c=0

for k,v in marks.items():
    if k==name:
        print(k, "\t\tyes,it's exist")
        c = 1
        break

if c == 0:
        print(name, "Not found")