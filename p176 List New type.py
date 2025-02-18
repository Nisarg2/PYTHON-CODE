list1=[]
n=int(input("Enter limit =>"))

for i in range(1,n+1):
    value=input("Enter name =>")
    list1.append(value)

print(list1)

searchvalue=input("Enter value for search ->")

if searchvalue in list1:
    print("It is there")
else:
    print("It is not there")
