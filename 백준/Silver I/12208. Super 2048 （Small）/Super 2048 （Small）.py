r = {'left' : 0, 'up' : 3, "right" : 2, "down" : 1}
def rotate(board):
    new_board = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_board[j][size-i-1] = board[i][j]
    return new_board
def operate(board):
    new_board = [[0] * size for _ in range(size)]
    for i in range(size):
        new_row = []
        prev = 0
        for j in range(size):
            if board[i][j] != 0:
                if prev == 0:
                    prev = board[i][j]
                elif prev == board[i][j]:
                    new_row.append(board[i][j]*2)
                    prev = 0
                else:
                    new_row.append(prev)
                    prev = board[i][j]
        if prev != 0:
            new_row.append(prev)
        for j in range(len(new_row)):
            new_board[i][j] = new_row[j]
    return new_board

for k in range(int(input())):
    size, b = input().split()
    size = int(size)
    b = r[b]
    board = [list(map(int, input().split())) for _ in range(size)]
    for i in range(b):
        board = rotate(board)
    board = operate(board)
    for i in range(4-b):
        board = rotate(board)
    print(f"Case #{k+1}:")
    for i in board:
        print(*i)