import sys
input = sys.stdin.readline

n, t = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]
trees.sort()
ans = 0
mx = trees[0][0]*t+trees[0][1]
mx_idx = 0
for i in range(1, n):
    ans += min(max(0, trees[mx_idx][1]-(trees[i][0]-trees[mx_idx][0])*t), trees[i][1])
    cand = trees[i][0]*t+trees[i][1]
    if mx < cand:
        mx = cand
        mx_idx = i
    #print(ans, mx, mx_idx, cand)
print(ans)