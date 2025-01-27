n=int(input("enter a limit=>"))
t=0
c=0
for i in range(1,n+1):
    if i % 2==0:
        print(i)
        t=t+i
        c=c+1
print("total =",t ,"count =",c)
