import random
n=int(input("enter limit=>"))
list1=[]
list2=[]
for i in range(1,n+1):
    y=random.randint(0,10)
    list1.append(y)

print(list1)

for i in list1:
    if i %7==0:
        list2.append(i)
        print(i)
print(list2)

