n = int(input())
m = int(input())
arr = [int(input()) for _ in range(m)]

dp = [0 for _ in range(41)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
for i in range(m):
    if i == 0:
        ans *= dp[arr[i]-1]
    else:
        ans *= dp[arr[i]-arr[i-1]-1]
if m: ans *= dp[n-arr[-1]]
else: ans = dp[n]

print(ans)