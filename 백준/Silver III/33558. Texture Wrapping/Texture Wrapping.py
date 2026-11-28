import sys
input = sys.stdin.readline

n, m = map(int, input().split())
u, v = map(int, input().split())
if u > n: u = n
if v > m: v = m
board = [list(input().rstrip()) for _ in range(u)]
q = input().rstrip()
if q == 'clamp-to-edge':
    ans = [['' for _ in range(m)] for _ in range(n)]
    for i in range(u):
        for j in range(v):
            ans[i][j] = board[i][j]
    for i in range(u, n):
        for j in range(v):
            ans[i][j] = board[u-1][j]
    for i in range(u):
        for j in range(v, m):
            ans[i][j] = board[i][v-1]
    for i in range(u, n):
        for j in range(v, m):
            ans[i][j] = board[u-1][v-1]
    for i in range(n):
        print(''.join(ans[i]))
elif q == 'repeat':
    ans = [['' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = board[i%u][j%v]
    for i in range(n):
        print(''.join(ans[i]))
else:
    ans = [['' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a, b = i//u, j//v
            if a%2: idx1 = u-1-i%u
            else: idx1 = i%u
            if b%2: idx2 = v-1-j%v
            else: idx2 = j%v
            ans[i][j] = board[idx1][idx2]
    for i in range(n):
        print(''.join(ans[i]))