n = int(input("Enter a limit => "))
total=0
for i in range(n,0,-1):
    print(i, end="X")
    total+=i
print("\ntotal sum",total)