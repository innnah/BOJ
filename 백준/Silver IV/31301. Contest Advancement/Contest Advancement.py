import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
school = [0 for _ in range(n+1)]
used = [0 for _ in range(n)]
ans = []
for i in range(n):
    if len(ans) == m: break
    if school[arr[i][1]] < k:
        ans.append([i, arr[i][0]])
        school[arr[i][1]] += 1
        used[i] = 1
if len(ans) >= m:
    for i in range(m):
        print(ans[i][1])
else:
    for i in range(n):
        if len(ans) == m: break
        if not used[i]:
            ans.append([i, arr[i][0]])
    ans.sort()
    for i in range(m):
        print(ans[i][1])