n=int(input("Enter A Number=>"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i%2,end="")
    print(" ")