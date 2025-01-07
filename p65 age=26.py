print(("press 1 for male"))
print("press 2 for female")
op=int(input("enter a opt"))
if op==1:
    age=int(input("enter a age"))
    if age>=18 and age<30:
        print("male wage=",700)
    else:
        print("female wage=",750)
elif op==2:
    age=int(input("enter a age"))
    if age>=30 and age<=40:
        print("male wage=",800)
    else:
        print("female wage=",850)
else:
    print("wrong opt")

