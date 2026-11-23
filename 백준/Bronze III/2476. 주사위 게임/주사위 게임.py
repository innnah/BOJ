import sys
input = sys.stdin.readline
ma = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b and b == c: ma = max(ma, 10000+a*1000)
    elif a == b or a == c: ma = max(ma, 1000+a*100)
    elif b == c: ma = max(ma, 1000+b*100)
    else: ma = max(ma, max(a, b, c)*100)
print(ma)