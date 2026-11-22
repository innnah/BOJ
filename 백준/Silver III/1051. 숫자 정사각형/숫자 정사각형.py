import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        k = 0
        ret = 0
        while i+k<n and j+k<m:
            if arr[i][j] == arr[i+k][j] and arr[i+k][j] == arr[i+k][j+k] and arr[i+k][j+k] == arr[i][j+k]:
                ret = max(ret, k+1)
            k += 1
        ans = max(ans, ret)
print(ans**2)