import time
current = time.localtime(time.time())
h=current.tm_hour
m=current.tm_min
s=current.tm_sec
t=current.tm_hour
if h>12:
    h=h-12
    print(h,":",m,":",s)

