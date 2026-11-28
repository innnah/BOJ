import sys
input = sys.stdin.readline

def get_dist(idx, x, y):
    return (players[idx][0] - x)**2 + (players[idx][1] - y)**2

n, m = map(int, input().split())
players = [list(map(int, input().split())) + [i] for i in range(n)]
ans = 0
skip = 0
for _ in range(m):
    x, y = map(int, input().split())
    p = []

    if skip:
        skip = 0
        continue

    for i in range(n):
        if get_dist(i, x, y) <= players[i][2]**2:
            p.append([players[i][3], i])
    p.sort()
    if p:
        if p[-1][1] == 0:
            ans += 1
    else:
        skip = 1
print(ans)