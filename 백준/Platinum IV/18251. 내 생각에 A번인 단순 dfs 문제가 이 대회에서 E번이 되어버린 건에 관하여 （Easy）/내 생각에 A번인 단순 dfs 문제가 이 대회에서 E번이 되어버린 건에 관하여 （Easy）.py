import sys
sys.setrecursionlimit(2**19)
input = sys.stdin.readline

def dfs(s, e, v, d):
    mid = (s+e)//2
    arr[mid] = l[v-1]
    depth_arr[mid] = d
    if s != e:
        dfs(s, mid-1, 2*v, d+1)
        dfs(mid+1, e, 2*v+1, d+1)

n = int(input())
l = list(map(int, input().split()))
arr = [0 for _ in range(n)]
depth_arr = [0 for _ in range(n)]
dfs(0, n-1, 1, 0)
depth = max(depth_arr)+1
ans = -float('inf')
for i in range(depth):
    for j in range(i, depth):
        psum, ret = 0, -float('inf')
        for k in range(n):
            if i <= depth_arr[k] <= j:
                psum += arr[k]
                ret = max(ret, psum)
                psum = max(0, psum)
        ans = max(ans, ret)
print(ans)