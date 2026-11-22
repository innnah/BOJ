prev = float(input())
while 1:
    s = float(input())
    if s == 999: break
    print("%0.2f" % (s-prev))
    prev = s