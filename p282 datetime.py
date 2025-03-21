import time
current = time.localtime(time.time())
d=current.tm_mday
m=current.tm_mon
y=current.tm_year

if m==1:
    print(d,"/Jan/",y)
elif m==2:
    print(d,"/Feb/",y)
elif m==3:
    print(d,"/March/",y)
