import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
q = deque()
for i in range(n-m-1):
    while q and q[-1][0] >= arr[i+1] - arr[i]:
        q.pop()
    q.append([arr[i+1]-arr[i], i])
ret = q[0][0] + arr[n-m-1] - arr[0]
for i in range(m):
    if q[0][1] <= i:
        q.popleft()
    while q and q[-1][0] >= arr[i+n-m] - arr[i+n-m-1]:
        q.pop()
    q.append([arr[i+n-m]-arr[i+n-m-1], i+n-m-1])
    ret = min(ret, q[0][0] + arr[i+n-m] - arr[i+1])
print(ret)