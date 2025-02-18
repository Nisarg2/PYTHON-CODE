list = [11, 44, 500, 22, 99, 77, 200, 66, 2]
t=0
c=0
for x in list:
    if x%2==0:
       t+=1

    else:
         c+=1
print("Even numbers:" ,t)
print("Odd numbers:", c)

