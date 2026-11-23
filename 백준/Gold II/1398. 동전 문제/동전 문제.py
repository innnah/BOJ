import sys
input = sys.stdin.readline

dp = [987654321 for _ in range(100)]
dp[0] = 0
dp[1] = dp[10] = dp[25] = 1
for i in range(1, 100):
    for j in [1, 10, 25]:
        if j > i: break
        dp[i] = min(dp[i], dp[i-j]+1)
for _ in range(int(input())):
    n = int(input())
    ret = 0
    while n > 0:
        ret += dp[n%100]
        n //= 100
    print(ret)