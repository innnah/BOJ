import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split()))[1] for _ in range(n)]
stack = []
cnt = 0
for i in range(n):
    if arr[i] == 0:
        stack = []
        continue
    while stack and stack[-1] > arr[i]:
        stack.pop()
    if not stack or arr[i] != stack[-1]:
        stack.append(arr[i])
        cnt += 1
print(cnt)