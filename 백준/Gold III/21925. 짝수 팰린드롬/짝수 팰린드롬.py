import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
cache = [[0] * n for _ in range(n)]
for i in range(n):
    idx1 = idx2 = i
    while idx1 >= 0 and idx2 < n and l[idx1] == l[idx2]:
        cache[idx1][idx2] = 1
        idx1 -= 1
        idx2 += 1
for i in range(n-1):
    idx1 = i
    idx2 = i+1
    while idx1 >= 0 and idx2 < n and l[idx1] == l[idx2]:
        cache[idx1][idx2] = 1
        idx1 -= 1
        idx2 += 1
start = 0
cnt = 0
for i in range(n):
    if cache[start][i] and (start-i+1) % 2 == 0:
        cnt += 1
        start = i+1
if start != n:
    print(-1)
else:
    print(cnt)