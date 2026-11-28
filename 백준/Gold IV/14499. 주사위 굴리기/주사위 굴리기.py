import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, m, y, x, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]
for i in orders:
    nx, ny = x + dx[i-1], y + dy[i-1]
    if 0<=nx<m and 0<=ny<n:
        if i == 1:
            dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
        elif i == 2:
            dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
        elif i == 3:
            dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
        else:
            dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
        if arr[ny][nx] == 0:
            arr[ny][nx] = dice[6]
        else:
            dice[6] = arr[ny][nx]
            arr[ny][nx] = 0
        x, y = nx, ny
        print(dice[1])