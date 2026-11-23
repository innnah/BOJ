import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
l = [list(map(int, input().rstrip())) for _ in range(n)]
ret = 0
for i in range(n):
    streak = 0
    for j in range(m):
        if l[i][j] == 1:
            ret += max(0, streak-k+1)
            streak = 0
        else:
            streak += 1
    ret += max(0, streak-k+1)
print(ret)