import random
d1={}
n=int(input("Enter limit =>"))

for i in range(1,n+1):
    eno=i
    esalary=random.randint(10000,50000)
    d1[eno]=esalary

print("Eno\t\tEname\t\tstatus")
print("*"*30)
for k,v in d1.items():
    if v>30000:
        print(k,"\t\t",v,"\t\tGood")
    else:
        print(k, "\t\t", v, "\t\tDo ur best")