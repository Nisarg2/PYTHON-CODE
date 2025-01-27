n=int(input("enter a limit=>"))
d=int(input("enter a limit=>"))
c=0
t=0
for i in range (1,n+1):
    if i % d==0:
        print(i)
        c=c+1
        t=t+1
print("count =",c,"total =", t)