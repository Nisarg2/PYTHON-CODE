import random
n=int(input("enter limit=>"))
list1=[]
for i in range(1,n+1):
    y=random.randint(0,10)
    list1.append(y)
print(list1)
list1.reverse()
print(list1)