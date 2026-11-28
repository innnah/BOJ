import sys
input = sys.stdin.readline

x, y = map(int, input().split())
cur = x*60 + y
n = int(input())
ans = 15000
for _ in range(n):
    xi, yi, di = map(int, input().split())
    t = xi*60 + yi
    while t < cur:
        t += di
    if t >= 1440:
        t = 1440 + xi*60 + yi
    ans = min(ans, t)
if ans >= 1440:
    ans -= 1440
print(f"{ans // 60:02d}:{ans % 60:02d}")