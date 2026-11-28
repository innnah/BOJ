import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    s1 = str(a*b)
    s2 = []
    a = str(a)[::-1]
    b = str(b)[::-1]
    for i in range(min(len(a), len(b))):
        s2.append(str(int(a[i]) * int(b[i])))
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            s2.append(a[i])
    else:
        for i in range(len(a), len(b)):
            s2.append(b[i])
    s2 = ''.join(s2[::-1])
    print(int(s1==s2))