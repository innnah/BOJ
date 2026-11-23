from collections import deque
dp = deque([1, 1, 1])
n = int(input())
if n < 4:
    print(1)
    exit(0)
for _ in range(4, n+1):
    dp.append(dp[0] + dp[2])
    dp.popleft()
print(dp[2])