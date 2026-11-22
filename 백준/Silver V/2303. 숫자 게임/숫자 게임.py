import itertools, sys
input = sys.stdin.readline

res = 0
res_val = -1
for i in range(int(input())):
    arr = list(map(int, input().split()))
    com = list(itertools.combinations(arr, 3))
    cand = 0
    for j in com:
        cand = max(cand, sum(j)%10)
    if cand >= res_val:
        res_val = cand
        res = i+1
print(res)