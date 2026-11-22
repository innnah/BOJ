import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
k = int(input())
apples = [tuple(map(int, input().split())) for _ in range(k)]
eaten = [0 for _ in range(k)]
l = int(input())
changes = [input().split() for _ in range(l)]
changes = [(int(x), c) for x, c in changes]
time = 0
d = 0
snake = deque([(1, 1)])
idx = 0
while time <= 11000:
    time += 1
    head = snake[0]
    nx, ny = head[0] + dx[d], head[1] + dy[d]
    if not (1 <= nx <= n and 1 <= ny <= n) or (nx, ny) in snake:
        break
    snake.appendleft((nx, ny))
    if (nx, ny) not in apples:
        snake.pop()
    else:
        tmp = apples.index((nx, ny))
        if not eaten[tmp]:
            eaten[apples.index((nx, ny))] = 1
        else:
            snake.pop()
    
    if idx < l and changes[idx][0] == time:
        if changes[idx][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        idx += 1
print(time)