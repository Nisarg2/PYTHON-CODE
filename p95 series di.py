n = int(input("Enter a limit => "))
total=0
for i in range(1,n+1):
    print("1/",i, end=" + ")
    total+=i
print("\ntotal sum",total)