import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and l[stack[-1]] < l[i]:
        answer[stack.pop()] = l[i]
    stack.append(i)

print(*answer)