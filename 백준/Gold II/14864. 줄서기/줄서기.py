import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ret = [i for i in range(1, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    ret[a-1] += 1
    ret[b-1] -= 1
a = list(sorted(ret))
if a != [i for i in range(1, n+1)]:
    print(-1)
else:
    print(*ret)