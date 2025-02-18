import random
n=int(input("Enter limit"))
list1=[]
for i in range(1,n+1):
    y=random.randint(-10,50)
    list1.append(y)
print(list1)
s=0
c=0

for x in list1:
    if x % 7 == 0:
        print(x)
        s=s+x
        c=c+1
print("sum = ",s)
print("count = ",c)