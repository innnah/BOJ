import time
now = time.localtime()
print("%4d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday))