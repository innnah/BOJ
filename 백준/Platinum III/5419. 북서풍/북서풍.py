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
for _ in range(int(input())):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    l.sort(key = lambda x:[x[0],-x[1]])
    for i in range(n):
        l[i] = l[i][1]
    a = list(sorted(l))
    dic = {a[i-1] : i for i in range(1, n+1)}
    arr = [dic[i] for i in l]
    tree = [0 for _ in range(100000)]
    ret = 0
    for i in range(n-1, -1, -1):
        ret += query(arr[i])
        update(arr[i], 1)
    print(ret)