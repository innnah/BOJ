import sys
input = sys.stdin.readline

def move(board, sm, direction):
    ret = [[0 for _ in range(n)] for _ in range(n)]
    maxval = sm
    if direction == 0:
        for i in range(n):
            idx = 0
            flag = True
            for j in range(n):
                if board[i][j] != 0:
                    if idx > 0 and ret[i][idx-1] == board[i][j] and flag:
                        ret[i][idx-1] *= 2
                        maxval = max(maxval, ret[i][idx-1])
                        flag = False
                    else:
                        ret[i][idx] = board[i][j]
                        idx += 1
                        flag = True
    if direction == 1:
        for i in range(n):
            idx = n-1
            flag = True
            for j in range(n-1, -1, -1):
                if board[i][j] != 0:
                    if idx < n-1 and ret[i][idx+1] == board[i][j] and flag:
                        ret[i][idx+1] *= 2
                        maxval = max(maxval, ret[i][idx+1])
                        flag = False
                    else:
                        ret[i][idx] = board[i][j]
                        idx -= 1
                        flag = True
    if direction == 2:
        for j in range(n):
            idx = 0
            flag = True
            for i in range(n):
                if board[i][j] != 0:
                    if idx > 0 and ret[idx-1][j] == board[i][j] and flag:
                        ret[idx-1][j] *= 2
                        maxval = max(maxval, ret[idx-1][j])
                        flag = False
                    else:
                        ret[idx][j] = board[i][j]
                        idx += 1
                        flag = True
    if direction == 3:
        for j in range(n):
            idx = n-1
            flag = True
            for i in range(n-1, -1, -1):
                if board[i][j] != 0:
                    if idx < n-1 and ret[idx+1][j] == board[i][j] and flag:
                        ret[idx+1][j] *= 2
                        maxval = max(maxval, ret[idx+1][j])
                        flag = False
                    else:
                        ret[idx][j] = board[i][j]
                        idx -= 1
                        flag = True
    return [maxval, ret]

best = 0
def solve(board, cnt, maxval):
    global best
    if maxval * (2 ** (5-cnt)) <= best: return
    best = max(best, maxval)
    if cnt == 5:
        return
    ne = [move(board, maxval, i) for i in range(4)]
    ne.sort(reverse = True)
    for i in range(4):
        if ne[i][1] != board:
            solve(ne[i][1], cnt + 1, ne[i][0])

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
sm = max([max(board[i]) for i in range(n)])
solve(board, 0, sm)
print(best)