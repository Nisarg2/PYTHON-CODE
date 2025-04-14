f1=open("abcd","r")
cnt=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        cnt=cnt+1
        print(ch,end="")


f1.close()
print("\ntotal vowels are",cnt)