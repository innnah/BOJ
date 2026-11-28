import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]
psum = [0 for _ in range(n+1)]
for i in range(n):
    psum[i] = psum[i-1] + arr[i]

dp[0] = arr[0]
stack = [(psum[0] + dp[0], 0)]
for i in range(1, n):
    idx = bisect.bisect(stack, (psum[i], n)) - 1
    if idx == -1:
        dp[i] = psum[i]
    else:
        idx2 = stack[idx][1]
        #print(i, stack, idx, idx2)
        dp[i] = psum[i] - psum[idx2]
    tmp = psum[i] + dp[i]
    while stack and stack[-1][0] >= tmp:
        stack.pop()
    stack.append((tmp, i))

ret = psum[n-1]
for i in range(n):
    ret = min(ret, max(dp[i], psum[n-1]-psum[i]))
    #print(i, dp[i], psum[n-1]-psum[i])
print(ret)