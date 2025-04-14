f1=open("abcd","r")
f2=open("abcd2","w")
f3=open("abcd3","w")
cnt=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        cnt=cnt+1
        f2.write(ch)
    else:
        f3.write(ch)
f1.close()
f2.close()
f3.close()
print("Copied")