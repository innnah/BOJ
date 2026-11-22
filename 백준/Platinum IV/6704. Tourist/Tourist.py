import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n = map(int, input().split())
    arr = [input().rstrip() for _ in range(n)]
    board = []
    for s in range(n+m-1):
        board.append([])
        for i in range(max(0, s-(m-1)), min(s, n-1)+1):
            j = s-i
            board[-1].append(arr[i][j])
    
    dp = [[[-10**20 for _ in range(min(n, m))] for _ in range(min(n, m))] for _ in range(n+m-1)]
    dp[0][0][0] = (board[0][0] == "*")
    for i in range(1, m):
        for j in range(len(board[i])):
            if board[i][j] == '#': continue
            for k in range(len(board[i])):
                if board[i][k] == '#': continue
                plus = (board[i][j] == "*") + (board[i][k] == "*") * (j != k)
                tmp = [1, 1, 1, 1]
                if j == 0: tmp[2], tmp[3] = 0, 0
                if j >= len(board[i-1]): tmp[0], tmp[1] = 0, 0
                if k == 0: tmp[1], tmp[3] = 0, 0
                if k >= len(board[i-1]): tmp[0], tmp[2] = 0, 0
                for p in range(2):
                    for q in range(2):
                        if tmp[p*2+q]: dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-p][k-q])
                dp[i][j][k] += plus
    
    for i in range(m, n+m-1):
        for j in range(len(board[i])):
            if board[i][j] == '#': continue
            for k in range(len(board[i])):
                if board[i][k] == '#': continue
                plus = (board[i][j] == "*") + (board[i][k] == "*") * (j != k)
                tmp = [1, 1, 1, 1]
                if j >= len(board[i-1])-1: tmp[2], tmp[3] = 0, 0
                if k >= len(board[i-1])-1: tmp[1], tmp[3] = 0, 0
                for p in range(2):
                    for q in range(2):
                        if tmp[p*2+q]: dp[i][j][k] = max(dp[i][j][k], dp[i-1][j+p][k+q])
                dp[i][j][k] += plus
    print(dp[-1][0][0])