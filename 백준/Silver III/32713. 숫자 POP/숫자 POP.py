import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sarr = sorted(arr)
d = {sarr[i] : i for i in range(n)}
arr = [d[arr[i]] for i in range(n)]
arr2 = [[] for _ in range(n)]
ren = [[0, -1]]
for i in range(1, n):
    if arr[i] != arr[i-1]:
        ren[-1][1] = i-1
        ren.append([i, -1])
ren[-1][1] = n-1

ans = -1
for i in range(len(ren)):
    ans = max(ans, ren[i][1] - ren[i][0] + 1)
    arr2[arr[ren[i][0]]].append(ren[i])

for i in range(n):
    for j in range(len(arr2[i])):
        s, d = arr2[i][j][1] - arr2[i][j][0] + 1, 0
        for k in range(j+1, len(arr2[i])):
            d += arr2[i][k][0] - arr2[i][k-1][1] - 1
            if d > m: break
            s += arr2[i][k][1] - arr2[i][k][0] + 1
        ans = max(ans, s)
print(ans)