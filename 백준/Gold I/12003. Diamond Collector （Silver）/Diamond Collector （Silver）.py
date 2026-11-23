import sys, bisect
input = sys.stdin.readline

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
l.sort()
dp = [bisect.bisect(l, l[i]+m) - i for i in range(n)]
for i in range(n-2, -1, -1):
    dp[i] = max(dp[i], dp[i+1])
dp.append(0)
ret = 0
for i in range(n):
    idx = bisect.bisect(l, l[i]+m)
    ret = max(ret, idx-i+dp[idx])
print(ret)