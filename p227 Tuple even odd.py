t1=(1,2,3,4,5)
c=0
s=0
for x in t1:
    if x%2==0:
        c=c+1
        s=s+x
        print(x)
print("count = ",c)
print("sum = ",s)