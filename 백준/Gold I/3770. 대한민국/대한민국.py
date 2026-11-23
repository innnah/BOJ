import sys
input = sys.stdin.readline

N = 1000
def query(v):
    ret = 0
    while v > 0:
        ret += tree[v]
        v -= (v & -v)
    return ret
def update(idx, num):
    while idx <= N:
        tree[idx] += num
        idx += (idx & -idx)
for t in range(int(input())):
    n, m, k = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    l = [tuple(map(int, input().split())) for _ in range(k)]
    l.sort()
    ret = 0
    for i in range(k):
        ret += query(N) - query(l[i][1])
        update(l[i][1], 1)
    print(f"Test case {t+1}: {ret}")