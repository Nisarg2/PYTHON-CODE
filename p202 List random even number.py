import random
n=int(input("enter limit=>"))
list1=[]
c=0
t=0
for i in range(1,n+1):
    y=random.randint(0,10)
    list1.append(y)

print(list1)

for i in list1:
    if i%2==0:
        c=c+1
        t=t+i
        print(i)
print("count = ",c)
print("total = ",t)
