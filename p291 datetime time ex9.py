import time

current = time.localtime(time.time())
print("Year:", current.tm_year)
print("Month:", current.tm_mon)
print("Date:", current.tm_year)
print("Day:", current.tm_mday)
print("Weekday:", current.tm_wday)
print("Yearday:", current.tm_yday)
print("Hour:", current.tm_hour)
print("Minutes:", current.tm_min)
print("Seconds:", current.tm_sec)