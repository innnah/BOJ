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

coor_n = int(input())
coors = [list(map(int, input().split())) for _ in range(coor_n)]
coors.sort(key = lambda x: (-x[1], x[0]))
n = 400005
tree = [0 for _ in range(400005)]
ret = 0
cnt = 0
equal_cnt = 0
for i in range(coor_n):
    update(coors[i][0] + 200001, 1)
    if cnt == 0 or coors[i][1] == coors[i-1][1]:
        cnt += 1
        if equal_cnt == 0 or coors[i][0] == coors[i-1][0]:
            equal_cnt += 1
        else:
            equal_cnt = 1
    else:
        cnt = 1
        equal_cnt = 1
    ret += (query(coors[i][0] + 200000)-cnt+equal_cnt) * (query(400004) - query(coors[i][0] + 200001))
    ret %= 1000000007
print(ret)