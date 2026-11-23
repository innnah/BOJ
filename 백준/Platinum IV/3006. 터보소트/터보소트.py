import sys
input = sys.stdin.readline

def query(v):
    ret = 0
    while v > 0:
        ret += tree[v]
        v -= (v & -v)
    return ret
def update(idx, num):
    while idx <= n:
        tree[idx] += num
        idx += (idx & -idx)

n = int(input())
b = [int(input()) for _ in range(n)]
arr = [0 for _ in range(n+1)]
for i in range(n):
    arr[b[i]] = i+1
tree = [0 for _ in range(n+1)]
i, j, a = 1, n, 1
while i <= j:
    if a:
        print(arr[i]-1 - query(arr[i]-1))
        a = 0
        update(arr[i], 1)
        i += 1
    else:
        print(n - arr[j] - query(n) + query(arr[j]))
        a = 1
        update(arr[j], 1)
        j -= 1