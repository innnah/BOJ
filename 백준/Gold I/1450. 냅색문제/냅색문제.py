import sys, bisect
input = sys.stdin.readline

def dfs(idx, cur, mode, size):
    if idx == size:
        sum[mode].append(cur)
        return
    dfs(idx+1, cur+a[mode][idx], mode, size)
    dfs(idx+1, cur, mode, size)

n, c = map(int, input().split())
arr = list(map(int, input().split()))
a = [arr[:n//2], arr[n//2:]]
sum = [[], []]
dfs(0, 0, 0, len(a[0]))
dfs(0, 0, 1, len(a[1]))
sum[0].sort()
sum[1].sort()
ret = 0
for i in sum[0]:
    ret += bisect.bisect(sum[1], c-i)
print(ret)