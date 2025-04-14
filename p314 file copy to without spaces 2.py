f1=open("abcd","r")
f2=open("abcd2","w")
while True:
    c = f1.read(1)
    if not c:
       break
    if c==" ":
        pass
    else:
       f2.write(c)
f1.close()
f2.close()
print("copied")

