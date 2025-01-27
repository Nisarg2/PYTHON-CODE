print("press 1 for xerox")
print("press 2 for typing")
op=int(input("enter a opt"))
if op==1:
    page=int(input("enter a page"))
    if page>50:
        print("rs is 5 =",page*5)
    else:
        print("rs is 8=",page*8)
elif op==2:
    page=int(input("enter a page"))
    if page>50:
        print("rs is 15=",page*15)
    else:
        print("rs is 20=",page*20)
else:
    print("wrong opt")
