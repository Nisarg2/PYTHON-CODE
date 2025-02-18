import random
n=int(input("Enter limit"))
list1=[]
list2=[]
list3=[]

for i in range(1,n+1):
    y=random.randint(-10,50)
    list1.append(y)
print(list1)

for x in list1:
    if x>0:
        list2.append(x)
    else:
        list3.append(y)

print("postive number = ",list2)
print("negtive number = ",list3)