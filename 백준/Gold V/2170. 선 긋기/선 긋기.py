import sys
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
ret = lines[0][1] - lines[0][0]
start, end = lines[0]
for i in range(1, n):
    if start <= lines[i][0] <= lines[i][1] <= end: continue
    ret += lines[i][1] - max(end, lines[i][0])
    if lines[i][0] > end:
        start = lines[i][0]
    end = lines[i][1]
print(ret)