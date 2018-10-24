
import calendar
import time
print(calendar.timegm(time.gmtime()))
def current_time():
    seconds = calendar.timegm(time.gmtime())
    curent_seconds = seconds % 60
    minutes = seconds // 60
    curent_minutes= minutes % 60
    hours = minutes // 60
    currenthour = hours % 24

    return curent_seconds, curent_minutes, currenthour

s,m,h = current_time()
print(h,m,s)




