n=int(input("enter a limit=>"))
total=0
for i in range(1,n+1):
    if i %2==0:
        total+=i*i
        print(i*i,end="+")
    else:
        total+=i*i*i
        print(i*i*i,end="+")
print("\n total sum",total)


