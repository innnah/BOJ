import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr2.append(0)
ans = arr.copy()

mx = deque([(arr[0], 0)])
i, j = 0, 0
t = 0
while i < n:
    ans[i] = max(ans[i], mx[0][0])
    if j+1 < n and t+arr2[j] <= arr[j+1]:
        t += arr2[j]
        while mx and mx[-1][0] <= arr[j+1]:
            mx.pop()
        mx.append((arr[j+1], j+1))
        j += 1
    else:
        if mx[0][1] == i:
            mx.popleft()
        t -= arr2[i]
        i += 1
        if i > j and i < n:
            j += 1
            mx.append((arr[j], j))
            t = 0

mx = deque([(arr[-1], n-1)])
i, j = n-1, n-1
t = 0
while j >= 0:
    ans[j] = max(ans[j], mx[0][0])
    if i > 0 and t+arr2[i-1] <= arr[i-1]:
        t += arr2[i-1]
        while mx and mx[-1][0] <= arr[i-1]:
            mx.pop()
        mx.append((arr[i-1], i-1))
        i -= 1
    else:
        if mx[0][1] == j:
            mx.popleft()
        t -= arr2[j-1]
        j -= 1
        if i > j and j >= 0:
            i -= 1
            mx.append((arr[i], i))
            t = 0
print(*ans)