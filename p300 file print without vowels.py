f1 = open("abcd","r")
while True:
    ch = f1.read(1)
    if not ch:
       break
    if ch=="a" or ch=="A" or ch=="e" or ch=="E" or ch=="i"or ch=="I" or ch=="o" or ch=="O" or ch=="u" or ch=="U":
        pass
    else:
        print(ch,end="")
f1.close()