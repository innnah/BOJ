import sys
from copy import deepcopy
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
best = 0
def isInside(x, y):
    return 0 <= x <= 3 and 0 <= y <= 3
def bruteforce(board, shark, ans):
    global best
    nos = [[-1, -1] for _ in range(17)]
    for x in range(4):
        for y in range(4):
            if board[x][y][0] != -1:
                nos[board[x][y][0]] = [x, y]
    for no in range(1, 17):
        x, y = nos[no]
        if x != -1 and y != -1:
            while 1:
                nx, ny = x + dx[board[x][y][1]], y + dy[board[x][y][1]]
                if isInside(nx, ny) and shark[0] != [nx, ny]:
                    nos[no] = [nx, ny]
                    if board[nx][ny][0] != -1:
                        nos[board[nx][ny][0]] = [x, y]
                    board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                    break
                board[x][y][1] = (board[x][y][1]+1)%8
    nx, ny = shark[0][0] + dx[shark[1]], shark[0][1] + dy[shark[1]]
    while 1:
        if not isInside(nx, ny): break
        if board[nx][ny][0] != -1:
            newboard = deepcopy(board)
            newshark = shark.copy()

            newshark[0] = [nx, ny]
            newshark[1] = board[nx][ny][1]
            newboard[nx][ny] = [-1, -1]
            bruteforce(newboard, newshark, ans + board[nx][ny][0])
        nx, ny = nx + dx[shark[1]], ny + dy[shark[1]]
    best = max(best, ans)

arr = [list(map(int, input().split())) for _ in range(4)]
board = [[[-1, -1] for _ in range(4)] for _ in range(4)]
shark = [[-1, -1], -1]
for i in range(4):
    for j in range(4):
        board[i][j][0] = arr[i][j*2]
        board[i][j][1] = arr[i][j*2+1] - 1
shark[0] = [0, 0]
shark[1] = board[0][0][1]
ans = board[0][0][0]
board[0][0] = [-1, -1]
bruteforce(board, shark, ans)
print(best)