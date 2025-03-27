f1 = open("abcd","r")
cnt=0
while True:
    c = f1.read(1)
    if not c:
       break
    if c==" ":
        cnt+=1

f1.close()
print("Total spaces are ",cnt)