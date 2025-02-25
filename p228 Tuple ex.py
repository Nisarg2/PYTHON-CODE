t1=(7,14,21,28,11,22,44,66,77)
c=0
s=0
for x in t1:
    if x%7==0:
        c=c+1
        s=s+x
        print(x)
print("count = ",c)
print("sum = ",s)