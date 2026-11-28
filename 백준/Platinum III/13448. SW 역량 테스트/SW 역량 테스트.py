import sys
input = sys.stdin.readline

n, t = map(int, input().split())
score = list(map(int, input().split()))
penalty = list(map(int, input().split()))
solve = list(map(int, input().split()))
problems = [[score[i], penalty[i], solve[i]] for i in range(n)]
problems.sort(key = lambda x : x[2]/x[1])
dp = [[-999999999999999999999999999] * (t+1) for i in range(n+1)]
dp[-1][0] = 0
for i in range(n):
    for j in range(min(problems[i][2], t+1)):
        dp[i][j] = max(dp[i][j], dp[i-1][j]-problems[i][0])
    for j in range(problems[i][2], t+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j]-problems[i][0], dp[i-1][j-problems[i][2]]-problems[i][1]*j)
print(sum(score)+max(dp[n-1]))