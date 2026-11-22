import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
p = [[-1, i] for i in range(n+1)]
for i in range(m):
    p[arr[i]] = [i, arr[i]]
p.sort()
ans = []
for i in range(n+1):
    if p[i][0] != -1:
        ans.append(p[i][1])
print(len(ans))
print(*ans)