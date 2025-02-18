no1=int(input("Enter starting no =>"))
no2=int(input("Enter ending no =>"))
for j in range(no1,no2+1):
    c=0
    no=j
    for i in range(2,no):
        if no%i==0:
            c=5
            break
    if c==0:
        print(no,end=" ")
