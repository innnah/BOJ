import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def isInside(x, y): return 0 <= x < 10 and 0 <= y < 10
def control(x, y, bitmask):
    bitmask[y] ^= (1 << x)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny): bitmask[ny] ^= (1 << nx)
def bruteForce(idx=0, current=0):
    global best
    if idx == 10:
        ret = 0
        tmp = bitmask.copy()
        for i in range(1, 10):
            for j in range(10):
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

d = {'#' : 0, 'O' : 1}
l = [list(input()) for _ in range(10)]
bitmask = [0 for _ in range(10)]
for i in range(10):
    for j in range(10):
        bitmask[i] |= d[l[i][j]] * (1 << j)
best = 105
bruteForce()
print(best if best != 105 else -1)