n=int(input("enter a limit=>"))
total=0
for i in range(1,n+1):
    print(i*i, end="+")
    total+=i*i
print("\n total sum",total)