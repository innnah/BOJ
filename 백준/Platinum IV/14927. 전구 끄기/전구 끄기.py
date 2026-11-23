dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0 <= x < n and 0 <= y < n
def control(x, y, bitmask):
    bitmask[y] ^= (1 << x)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny): bitmask[ny] ^= (1 << nx)
def bruteForce(idx=0, current=0):
    global best
    if idx == n:
        ret = 0
        tmp = bitmask.copy()
        for i in range(1, n):
            for j in range(n):
                if tmp[i-1] & (1 << j):
                    control(j, i, tmp)
                    ret += 1
        if tmp[-1] == 0:
            best = min(best, current+ret)
        return
    control(idx, 0, bitmask)
    bruteForce(idx+1, current+1)
    control(idx, 0, bitmask)
    bruteForce(idx+1, current)

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
bitmask = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        bitmask[i] |= l[i][j] * (1 << j)
best = n**2+5
bruteForce()
print(best if best != n**2+5 else -1)