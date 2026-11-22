a, b, c = map(int, input().split())
s = (a+b+c)/2
s1, s2, s3 = s-c, s-b, s-a
if s1 > 0 and s2 > 0 and s3 > 0:
    print(1)
    print("%.1f %.1f %.1f" % (s1, s2, s3))
else:
    print(-1)