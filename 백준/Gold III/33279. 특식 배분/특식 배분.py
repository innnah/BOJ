import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [-1 for _ in range(n+1)]
dp_psum = [0 for _ in range(n+2)]
dp[0] = 0
for i in range(1, n+1):
    dp[i] = (dp_psum[i-1] - dp_psum[i-arr[i-1]-1]) / arr[i-1] + 1
    dp_psum[i] = dp[i] + dp_psum[i-1]
print(dp[n])