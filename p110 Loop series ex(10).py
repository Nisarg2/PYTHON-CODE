n=int(input("enter a limit=>"))
total=0
for i in range(1,n+1):
    print(i,end="+")
    total+=i
print("\ntotal sum:",total)