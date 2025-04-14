f1=open("abcd","r")
f2=open("abcd2","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        f2.write("7")
    else:
        f2.write(ch)
f1.close()
f2.close()
print("copied")