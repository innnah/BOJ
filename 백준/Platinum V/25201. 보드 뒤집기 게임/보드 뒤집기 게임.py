import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r = [0 for _ in range(100001)]
c = [0 for _ in range(100001)]
for _ in range(n+m):
    a, b = map(int, input().split())
    r[a] += 1
    c[b] += 1
for i in range(100001):
    if r[i] % 2 or c[i] % 2:
        print("NO")
        break
else:
    print("YES")