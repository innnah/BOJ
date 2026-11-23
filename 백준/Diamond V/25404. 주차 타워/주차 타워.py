import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dpf(val, idx):
    if val == len(sarr):
        return 0
    if dp[idx] != -1:
        return dp[idx]
    
    p1 = left[idx]
    move1 = n - (idx - p1) % n
    p2 = right[idx]
    move2 = n - (p2 - idx) % n

    if len(nums[val]) == 1:
        move1, move2 = 0, 0

    if val+1 == len(sarr):
        return min(move1, move2)
    
    dp[idx] = 10**20
    for i in nums[val+1]:
        dp[idx] = min(dp[idx], min(min(n-abs(p1-i), abs(p1-i))+move1,min(n-abs(p2-i), abs(p2-i))+move2)+dpf(val+1, i))
    return dp[idx]

n = int(input())
arr = list(map(int, input().split()))
sarr = sorted(list(set(arr)))
d = {sarr[i] : i for i in range(len(sarr))}
arr = [d[arr[i]] for i in range(n)]
nums = [[] for _ in range(len(sarr))]
left = [0 for _ in range(n)]
right = [0 for _ in range(n)]
for i in range(n):
    nums[arr[i]].append(i)
for i in range(len(sarr)):
    for j in range(len(nums[i])):
        left[nums[i][(j+1)%len(nums[i])]] = nums[i][j]
        right[nums[i][j]] = nums[i][(j+1)%len(nums[i])]

dp = [-1 for _ in range(n)]
ret = 10**20
for i in range(n):
    if arr[i] == 0:
        ret = min(ret, min(i, n-i) + dpf(0, i))
print(ret)