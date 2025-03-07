students = {73: "mohan", 25: "rahul", 66: "dev",89: "sita", 30: "arjun", 35: "krishna", 20: "raj"}
print("press1 for only pass")
print("press2 for only fail")
print("press3 for both")
no=int(input("enter the num=>"))

if no==1:
    for k,v in students.items():
        if k>=35:
            print(k,"\t\t",v,"\t\t pass")
elif no==2:
    for k,v in students.items():
        if k<=35:
            print(k,"\t\t",v,"\t\t fail")
elif no==3:
    for k,v in students.items():
        if k>=35:
            print(k,"\t\t",v,"\t\t pass")
        else:
            print(k,"\t\t", v, "\t\tfail")
else:
    print(no, "is wrong opt")