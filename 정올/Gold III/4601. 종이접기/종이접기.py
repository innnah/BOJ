import sys
from collections import defaultdict

k = int(input())
folds = input().split()
h = int(input())
no = [defaultdict(int) for _ in range(4)]
no[0]['D'] = 2
no[1]['D'] = 3
no[2]['D'] = 0
no[3]['D'] = 1
no[0]['U'] = 2
no[1]['U'] = 3
no[2]['U'] = 0
no[3]['U'] = 1
no[0]['R'] = 1
no[1]['R'] = 0
no[2]['R'] = 3
no[3]['R'] = 2
no[0]['L'] = 1
no[1]['L'] = 0
no[2]['L'] = 3
no[3]['L'] = 2
l = [[-1] * (2**k) for _ in range(2**k)]
def solve(l, oridx):
    n = len(l)
    if oridx == k*2:
        return [[h]]
    order = folds[oridx]
    recur = []
    if order == 'D':
        for i in range(n//2, n):
            recur.append(l[i])
    if order == 'U':
        for i in range(n//2):
            recur.append(l[i])
    if order == 'R':
        for i in range(n):
            recur.append(l[i][n//2:n])
    if order == 'L':
        for i in range(n):
            recur.append(l[i][:n//2])
    ret = solve(recur, oridx+1)
    tmp = [[] for _ in range(len(ret))]
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            tmp[i].append(no[ret[i][j]][order])
    if order in ('D','U'): tmp = tmp[::-1]
    else:
        for i in range(len(tmp)):
            tmp[i] = tmp[i][::-1]
    if order == 'D':
        for i in range(len(ret)):
            tmp.append(ret[i])
        return tmp
    if order == 'U':
        for i in range(len(tmp)):
            ret.append(tmp[i])
        return ret
    if order == 'R':
        for i in range(len(ret)):
            for j in range(len(ret[i])):
                tmp[i].append(ret[i][j])
        return tmp
    if order == 'L':
        for i in range(len(ret)):
            for j in range(len(tmp[i])):
                ret[i].append(tmp[i][j])
        return ret
ret = solve(l, 0)
for i in ret:
    print(*i)