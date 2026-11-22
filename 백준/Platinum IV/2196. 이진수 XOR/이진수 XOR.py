import sys
from collections import deque
input = sys.stdin.readline

def bitcomp(a, b):
    return bin(a^b).count("1")
def bfs():
    q = deque([[nums[i], 0] for i in range(m)])
    ret = [n+1, 0, 0]
    while q:
        v, d = q.popleft()
        if d >= 1:
            ret = min(ret, [bitcomp(v, target), d, v])
        for i in range(m):
            if dp[v^nums[i]] == -1 or dp[v^nums[i]] < 1:
                dp[v^nums[i]] = d+1
                q.append([v^nums[i], d+1])
    return ret

n, m = map(int, input().split())
target = int(input(), 2)
nums = list(set([int(input(), 2) for _ in range(m)]))
m = len(nums)
dp = [-1 for _ in range(2**n)]
ans = bfs()
print(ans[1])
ret = bin(ans[2])[2:]
print("0"*(n-len(ret)) + ret)