n=int(input("enter a limit=>"))
total=0
for i in range(1,n+1):
    if i % 2==0:
        pass
    else:
        print(i, end="+")
        total+=i
print("\n total sum",total)