n=int(input("enter a limit=>"))
d=int(input("enter a limit=>"))
for i in range (1,n+1):
    if i % d==0:
        print(i)