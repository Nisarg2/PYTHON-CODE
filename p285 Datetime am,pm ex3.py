import time
current = time.localtime(time.time())
h=current.tm_hour
m=current.tm_min
s=current.tm_sec
if 24<=h<12:
    print(h, ":", m, ":", s,"AM")
else :
    print(h, ":", m, ":", s,"PM")