f1=open("abcd","r")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        pass
    else:
        print(ch,end="8")



f1.close()