print("press 1 for battery based toy")
print("press 2 for key based toy")
print("press 3 for electrical based toy")
op=int(input("enter a your opt"))
if op==1:
     print("battery based toy")
     money=int(input("enter your amount"))
     if money>1000:
         print("you got a 10 disccount=",1000*10/100)
     else:
         print("you have no disccount")
elif op==2:
     print("key ased toy")
     money=int(input("enter your amount"))
     if money>100:
         print("you got a 5 disccount=",100*5/100)
     else:
         print("you have no disccount")

elif op==3:
     print("electrical based toy")
     money=int(input("enter your amount"))
     if money>500:
         print("you got a 10 disccount=",500*10/100)
     else:
         print("you have no disccount")
else:
     ("wrong opt")
