import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

r = [[0, 0] for _ in range(n)]
c = [[0, 0] for _ in range(m)]
r1_val = []
r[0] = [1, 0]
r1_val.append(0)

for i in range(m):
    c[i] = [-1, board[0][i]]
    r1_val.append(board[0][i])

for i in range(1, n):
    r[i] = [1, board[i][0] - board[0][0]]
    r1_val.append(board[0][0] - board[i][0])

r1_val.sort()
r1_val.append(-10**12)

r1 = 0
f = 0
start = 0
for i in range(1, len(r1_val)):
    if r1_val[i] != r1_val[i-1]:
        cand = i-start
        if cand > f:
            f = cand
            r1 = r1_val[i-1]
        start = i

sboard = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    val = r1*r[i][0] + r[i][1]
    for j in range(m):
        sboard[i][j] += val
for i in range(m):
    val = r1*c[i][0] + c[i][1]
    for j in range(n):
        sboard[j][i] += val
if sboard != board:
    print(-1)
else:
    print(n+m-f)
    for i in range(n):
        val = r1*r[i][0] + r[i][1]
        if val: print(1, i+1, val)
    for i in range(m):
        val = r1*c[i][0] + c[i][1]
        if val: print(2, i+1, val)