import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def select(picked):
    global best
    if len(picked) > m: return
    cd = 0
    if picked:
        for i in range(len(houses)):
            mini = 987654321
            for j in picked:
                mini = min(mini, distance[i][j])
            cd += mini
        best = min(best, cd)
    if picked: first = picked[-1]
    else: first = -1
    for i in range(first+1, len(chickens)):
        picked.append(i)
        select(picked)
        picked.pop()

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            houses.append((j, i))
        elif l[i][j] == 2:
            chickens.append((j, i))
distance = [[0] * len(chickens) for _ in range(len(houses))]
for i in range(len(houses)):
    for j in range(len(chickens)):
        hx, hy, cx, cy = houses[i][0], houses[i][1], chickens[j][0], chickens[j][1]
        distance[i][j] = abs(hx-cx) + abs(hy-cy)
best = 987654321
select([])
print(best)