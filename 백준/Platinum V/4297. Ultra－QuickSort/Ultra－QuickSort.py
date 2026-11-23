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

while True:
    n = int(input())
    if n == 0: break
    b = [int(input()) for _ in range(n)]
    tmp = sorted(list(set(b)))
    dic = {tmp[i] : i+1 for i in range(len(tmp))}
    b = [dic[i] for i in b]
    arr = [0 for _ in range(n+1)]
    for i in range(n):
        arr[b[i]] = i+1
    ret = 0
    tree = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        ret += query(n) - query(arr[i])
        update(arr[i], 1)
    print(ret)