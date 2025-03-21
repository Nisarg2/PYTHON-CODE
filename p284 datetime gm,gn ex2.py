import time
current=time.localtime(time.time())
t=current.tm_hour
if 5 <= t< 12:
    print("Good morning!")
elif 12 <=t<18:
    print("Good afternoon!")
elif 18 <=t< 22:
    print("Good evening!")
else:
    print("Good night!")
