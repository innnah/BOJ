import sys
input = sys.stdin.readline

MOD = 10**9+7
def get_psum(lb, lr):
    if lb%2 == lr%2:
        return psum[lr-1] - psum[lb-1]
    return psum[lr-1] - psum[lb-2]

n = int(input())
s = input().rstrip()
left_b = [0 for _ in range(n)]
left_r = [0 for _ in range(n)]
right_b = [0 for _ in range(n)]

b_idx = -1
r_idx = -1
for i in range(n):
    if s[i] == 'B': b_idx = i
    left_b[i] = b_idx
    if s[i] == 'R': r_idx = i
    left_r[i] = r_idx
b_idx = n
for i in range(n-1, -1, -1):
    if s[i] == 'B': b_idx = i
    right_b[i] = b_idx

dp = [0 for _ in range(n+1)]
dp[-1] = 1
psum = [0 for _ in range(n+2)]
psum[-1] = 1
psum[-2] = 1
for i in range(n):
    if s[i] not in 'BR':
        dp[i] = dp[i-1]
    x = 1
    limit = i-left_r[i]
    while x <= limit and i - 2*x + 1 >= 0:
        lred = i - 2*x + 1
        lblue = i - x + 1
        if right_b[lred] < lblue:
            x = i + 1 - right_b[lred]
        else:
            ret = get_psum(max(left_b[lred], i-2*limit), lred)
            dp[i] += ret
            x = (i - left_b[lred])//2 + 1
        #print(i, x, dp[i])
    psum[i] = psum[i-2] + dp[i]
    psum[i] %= MOD
    dp[i] %= MOD
print(dp[n-1])