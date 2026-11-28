import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
cows = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True)
towers = deque([[10**20, m]])
ans = 0
for w, a in cows:
    remain = a
    while len(towers) > 0 and remain > 0 and w+k <= towers[0][0]:
        if towers[0][1] > remain:
            towers[0][1] -= remain
            remain = 0
        else:
            remain -= towers[0][1]
            towers.popleft()
    if remain != a:
        towers.append([w, a-remain])
        ans += a-remain
print(ans)