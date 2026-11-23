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
b = list(map(int, input().split()))
x, y = 0, 0
ret = 0
while y < n-1:
    if b[y] >= b[y+1]:
        y += 1
    else:
        b[x:y+1] = list(reversed(b[x:y+1]))
        ret += 1
        x = y+1
        y = x
if y != x: 
    b[x:y+1] = list(reversed(b[x:y+1]))
    ret += 1
arr = [0 for _ in range(n+1)]
for i in range(n):
    arr[b[i]] = i+1
tree = [0 for _ in range(n+1)]
for i in range(1, n+1):
    ret += query(n) - query(arr[i])
    update(arr[i], 1)
print(ret)