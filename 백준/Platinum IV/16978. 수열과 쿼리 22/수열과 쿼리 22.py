import sys
input = sys.stdin.readline

def query(v):
    if v == 0: return 0
    ret = 0
    while v > 0:
        ret += tree[v]
        v -= (v & -v)
    return ret
def update(idx, num):
    tmp = idx-1
    while idx <= n:
        tree[idx] += num - l[tmp]
        idx += (idx & -idx)
n = int(input())
l = list(map(int, input().split()))
tree = [0 for _ in range(n+1)]
for i in range(1, n+1): 
    update(i, l[i-1]*2)
m = int(input())
q = [list(map(int, input().split())) for _ in range(m)]
upd = [[]]
qu = [[] for _ in range(100005)]
for i in range(m):
    if q[i][0] == 1: upd.append([q[i][1], q[i][2]])
    else:
        qu[q[i][1]].append((q[i][2], q[i][3], i))
ret = [0 for _ in range(m+1)]
i = 0
while i < len(upd):
    if i != 0: 
        update(upd[i][0], upd[i][1])
        l[upd[i][0]-1] = upd[i][1]
    for j in range(len(qu[i])):
        ret[qu[i][j][2]] = query(qu[i][j][1]) - query(qu[i][j][0]-1)
    i += 1
for i in ret:
    if i != 0: print(i)