import time as t

st = t.struct_time(tm_year=2021, tm_mon=12, tm_mday=12,
              tm_hour=23, tm_min=21, tm_sec=13,
              tm_wday=6, tm_yday=346, tm_isdst=0)

x = 5                   #in seconds

s = t.time()            #time (in s) since epoch

t.ctime(s)              #current time (ctime takes epoch as arg)
t.sleep(x)              #pause program for x seconds
t.localtime()           #outputs current local time in struct_time
t.asctime(st)           #returns time in string format
