import sys

input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l = sorted(l, key = lambda x : (x[1], x[0]))
cnt = 1
idx = 0

for i in range(1, n):
    if l[i][0] >= l[idx][1]:
        cnt += 1
        idx = i

print(cnt)