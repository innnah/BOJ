import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
n = int(input())

for i in range(n):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])