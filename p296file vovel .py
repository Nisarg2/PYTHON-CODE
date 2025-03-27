f1=open("abcd","r")
cnt=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a" or ch=="A" or ch=="e" or ch=="E" or ch=="i"or ch=="I" or ch=="o" or ch=="O" or ch=="u" or ch=="U" :
        cnt=cnt+1

f1.close()
print("total vowels are",cnt)