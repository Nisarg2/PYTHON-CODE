f1 = open("abcd","r")
while True:
    c = f1.read(1)
    if not c:
       break
    if c==" ":
        pass
    else:
        print(c,end="")
f1.close()

