import sys
input = sys.stdin.readline

d = {"W": 0, "G": 1, "B": 2}
def solve():
    n, a, b = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    board = [[d[j] for j in i] for i in board]
    stars = [[0 for _ in range(n)] for _ in range(n)]
 
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                stars[i][j] = 1
                if i < b or j < a:
                    print(-1)
                    return
                if board[i-b][j-a] == 0:
                    print(-1)
                    return
                stars[i-b][j-a] = 1
 
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if stars[i][j] == 1:
                    continue
                if i < b or j < a:
                    stars[i][j] = 1
                    continue
                if stars[i-b][j-a] == 1:
                    continue
                stars[i][j] = 1
                    
    print(sum([sum(i) for i in stars]))
for _ in range(int(input())):
    solve()