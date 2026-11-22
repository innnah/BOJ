a, b = map(int, input().split())
v = int((a*a-b)**0.5)
c, d = -a - v, -a + v
if c == d: print(c)
else: print(c, d)