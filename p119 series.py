n=int(input("enter limit=>"))
total=0
for i in range(1,n+1):
    if i% 2==0:
        print(i,end="-")
        total-=i
    else:
        total+=i
        print(i,end="+")
print("\n total sum",total)