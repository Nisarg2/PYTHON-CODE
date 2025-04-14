f1=open("abcd","r")
f2=open("abcd2","w")
cnt=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        pass
    else:
        f2.write(ch)
f1.close()
f2.close()
print("Copied")