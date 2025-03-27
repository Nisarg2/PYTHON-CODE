f1=open("abcd","r")
cnt=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        cnt=cnt+1

f1.close()
print("total vowels are",cnt)