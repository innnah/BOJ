import sys
input = sys.stdin.readline
s0, n, m = map(int, input().split())
s, k = s0, 0
for _ in range(n+m):
    a = int(input())
    if a == 1:
        k += 1
        if s < k:
            s *= 2
    else:
        k -= 1
print(s)