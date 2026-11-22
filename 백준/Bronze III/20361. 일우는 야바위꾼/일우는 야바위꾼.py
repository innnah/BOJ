import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())
d = [i for i in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    d[a], d[b] = d[b], d[a]
for i in range(1, n+1):
    if d[i] == x:
        print(i)