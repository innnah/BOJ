import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
p = list(map(int, input().split()))
dp = [0 for _ in range(2**n)]
value = [0 for _ in range(2**n)]
for i in range(2**n):
    cnt = 0
    for j in range(n):
        if i & (1 << j):
            value[i] += arr[j]
            cnt += 1
    tmp = p[m] * (value[i] // m)
    if value[i] % m == 0:
        tmp += (cnt - value[i] // m) * p[0]
    else:
        tmp += (cnt - value[i] // m - 1) * p[0]
        tmp += p[value[i] % m]
    value[i] = tmp
for i in range(1, 2**n):
    ss = i
    while ss:
        dp[i] = max(dp[i], dp[ss] + value[ss ^ i])
        ss = (ss-1) & i
    dp[i] = max(dp[i], value[i])
print(dp[-1])