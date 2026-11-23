import sys, math
input = sys.stdin.readline

n, t = map(int, input().split())
orn = n
d = {}
for _ in range(t):
    a, b = input().rstrip().split()
    if b[-1] == '%':
        p = int(b[:-1])
        d[a] = (n, n*p//100)
        n -= d[a][1]
    else:
        p = int(b)
        d[a] = (n, min(n, p))
        n -= min(n, p)
if n != 0:
    print("Invalid System")
    sys.exit(0)
s = input().rstrip()
if s[-1].isnumeric():
    tier = s[:-1]
    c = d[tier][1]
    l = int(s[-1])
    t = []
    left = c
    for i in range(4):
        t.append(min(left, (c+3)//4))
        left -= t[-1]
    if t[l-1] == 0: print("Liar")
    else:
        st = orn-d[tier][0]+sum(t[:l-1])+1
        en = st+t[l-1]-1
        print(st, en)
else:
    tier = s
    c = d[tier][1]
    if c <= 0: print("Liar")
    else:
        st = orn-d[tier][0]+1
        en = st+c-1
        print(st, en)