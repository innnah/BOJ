def issquare(n): return int(n ** 0.5) ** 2 == n
l = []
g = int(input())
s = 1
while True:
    if (s+1) ** 2 - s ** 2 > g: break
    if issquare(s**2+g): l.append(int((s**2+g)**0.5))
    s += 1
if len(l) == 0: print(-1)
else:
    for i in l:
        print(i)