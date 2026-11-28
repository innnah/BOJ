import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lines = []
for i in range(n):
    for j in range(i+1, n):
        lines.append([(arr[j]-arr[i])/(j-i), j, i])
lines.sort()

dp = [1 for _ in range(n+1)]
for line in lines:
    dp[line[1]] = max(dp[line[1]], dp[line[2]]+1)
print(n-max(dp))