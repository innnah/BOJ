import sys
input = sys.stdin.readline

MOD = 10**9 + 7
ncr = [[0 for _ in range(2001)] for _ in range(2001)]
ncr[0][0] = 1
for i in range(1, 2001):
    ncr[i][0] = 1
    for j in range(1, i+1):
        ncr[i][j] = ncr[i-1][j] + ncr[i-1][j-1]
        ncr[i][j] %= MOD

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 1
    if arr == [1] * n:
        print(1)
        continue
    for i in range(n):
        ans *= ncr[n][arr[i]]
        n -= arr[i]
        ans %= MOD
    print(ans)