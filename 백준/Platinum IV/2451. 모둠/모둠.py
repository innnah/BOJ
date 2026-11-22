import sys
input = sys.stdin.readline

n = int(input())
friends = [list(map(int, input().split()))[:-1] for _ in range(n)]
is_friend = [[False for _ in range(n)] for _ in range(n)]
psum_friend = [[0 for _ in range(n+1)] for _ in range(n)]
for i in range(n):
    for j in friends[i]:
        is_friend[i][j-1] = True

for i in range(n):
    for j in range(n):
        psum_friend[i][j] = psum_friend[i][j-1] + is_friend[i][j]

dp = [10**9 for _ in range(n+1)]
dp[-1] = 0
trace = [-1 for _ in range(n+1)]
for i in range(n):
    score = 0
    for j in range(i-1, -2, -1):
        f1, f2 = psum_friend[j+1][i] - psum_friend[j+1][j+1], psum_friend[j+1][n-1] - psum_friend[j+1][i]
        score += i - (j+1) - f1 + f2
        dp[i] = min(dp[i], dp[j] + score)
        if dp[i] == dp[j] + score:
            trace[i] = j
print(dp[n-1])

ans = []
idx = n-1
while idx != -1:
    ans.append(idx - trace[idx])
    idx = trace[idx]
print(len(ans), end = ' ')
print(*ans[::-1])