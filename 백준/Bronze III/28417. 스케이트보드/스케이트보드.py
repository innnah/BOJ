import sys
input = sys.stdin.readline
s = 0
for _ in range(int(input())):
    l = list(map(int, input().split()))
    a, b = l[:2], l[2:]
    b.sort()
    s = max(s, max(a)+b[-2]+b[-1])
print(s)