import sys
input = sys.stdin.readline

def query(k, m, v, s, e):
    if k < s: return False
    if e <= k:
        return tree[v] <= m
    mid = (s + e) // 2
    return query(k, m, v*2, s, mid) or query(k, m, v*2+1, mid+1, e)
    
def update(idx, val, v, s, e):
    if idx < s or idx > e: return tree[v]
    if s == e: 
        tree[v] = val
        return tree[v]
    mid = (s + e) // 2
    tree[v] = min(update(idx, val, v*2, s, mid), update(idx, val, v*2+1, mid+1, e))
    return tree[v]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
arr = [[0,0,0] for _ in range(n)]
for i in range(n):
    arr[a[i]-1][0] = i+1
    arr[b[i]-1][1] = i+1
    arr[c[i]-1][2] = i+1
arr.sort()
tree = [0 for _ in range(4*n+10)]
for i in range(n):
    update(i+1, 10**10, 1, 1, n)
cnt = n
for i in range(n):
    if query(arr[i][1]-1, arr[i][2]-1, 1, 1, n):
        cnt -= 1
    update(arr[i][1], arr[i][2], 1, 1, n)
print(cnt)