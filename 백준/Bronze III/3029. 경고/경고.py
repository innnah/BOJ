h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
sec1 = h1*3600+m1*60+s1
sec2 = h2*3600+m2*60+s2
if sec1 >= sec2:
    sec2 += 86400
time = sec2-sec1
print(f"%02d:%02d:%02d" % (time//3600, (time%3600)//60, time%60))