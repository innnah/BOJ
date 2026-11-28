import sys
input = sys.stdin.readline

def query(v):
    ret = 0
    while v > 0:
        ret += tree[v]
        v -= (v & -v)
    return ret
def update(idx, num):
    while idx <= 10**6+1:
        tree[idx] += num
        idx += (idx & -idx)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
tree = [0 for _ in range(10**6+2)]
ans = 0
for i in range(n):
    limit = m-arr[i][0]
    update(arr[i][1]+1, 1)
    ans = max(ans, query(limit+1))
print(ans)