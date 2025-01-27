n = int(input("Enter a limit => "))
t=0
c=0
for i in range(1,n+1):
    if i % 2 == 0:
        print("even num =",i)
    else:
        print("odd num =",i)
    t=t+i
    c=c+1
print("Total =",t,"count =",c)