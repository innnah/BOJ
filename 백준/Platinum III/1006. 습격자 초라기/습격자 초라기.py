import sys
input = sys.stdin.readline

def dpf(start):
    for i in range(start, n):
        # 3
        if arr2[i] + arr2[i-1] <= a: dp[i][3] = dp[i-2][0] + 1
        # 4
        if arr1[i] + arr1[i-1] <= a: dp[i][4] = dp[i-2][0] + 1
        # 1
        dp[i][1] = min(dp[i-1][0], dp[i][3]) + 1
        if arr2[i] + arr2[i-1] <= a: dp[i][1] = min(dp[i][1], dp[i-1][2] + 1)
        # 2
        dp[i][2] = min(dp[i-1][0], dp[i][4]) + 1
        if arr1[i] + arr1[i-1] <= a: dp[i][2] = min(dp[i][2], dp[i-1][1] + 1)
        # 0
        dp[i][0] = min(dp[i][1], dp[i][2]) + 1
        if arr1[i] + arr2[i] <= a: dp[i][0] = min(dp[i][0], dp[i-1][0] + 1)
        if arr1[i] + arr1[i-1] <= a: dp[i][0] = min(dp[i][0], dp[i][3] + 1)
        if arr2[i] + arr2[i-1] <= a: dp[i][0] = min(dp[i][0], dp[i][4] + 1)

INF = 10**10
for _ in range(int(input())):
    n, a = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    ans = []

    dp = [[INF for _ in range(5)] for _ in range(n+1)]
    dp[-1] = [0, 0, 0, 0, 0]
    if arr1[0] + arr2[0] <= a: dp[0][0] = 1
    else: dp[0][0] = 2
    dp[0][1] = dp[0][2] = 1
    dpf(1)
    ans.append(dp[n-1][0])

    if arr1[0] + arr1[-1] <= a:
        dp = [[INF for _ in range(5)] for _ in range(n+1)]
        dp[0][0] = 2
        dp[0][2] = 1
        dpf(1)
        ans.append(dp[n-1][1])
    if arr2[0] + arr2[-1] <= a:
        dp = [[INF for _ in range(5)] for _ in range(n+1)]
        dp[0][0] = 2
        dp[0][1] = 1
        dpf(1)
        ans.append(dp[n-1][2])
    if arr1[0] + arr1[-1] <= a and arr2[0] + arr2[-1] <= a:
        dp = [[INF for _ in range(5)] for _ in range(n+1)]
        dp[0][0] = 2
        dpf(1)
        ans.append(dp[n-2][0])
    print(min(ans))