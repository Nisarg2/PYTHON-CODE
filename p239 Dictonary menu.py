import random
d1={}
n=int(input("Enter limit =>"))

for i in range(1,n+1):
    eno=i
    esalary=random.randint(10000,50000)
    d1[eno]=esalary

print("Eno\t\tEname")
for k,v in d1.items():
    print(k,"\t\t",v)