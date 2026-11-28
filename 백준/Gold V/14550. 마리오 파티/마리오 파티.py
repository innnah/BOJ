import sys
input = sys.stdin.readline

while 1:
    tmp = input().rstrip()
    if tmp == "0":
        break
    n, m, k = map(int, tmp.split())
    cnt = 0
    arr = [0]
    while cnt < n:
        tmp = list(map(int, input().split()))
        arr += tmp
        cnt += len(tmp)
    arr.append(0)
    dp = [[-10**20 for _ in range(k+1)] for _ in range(n+2)]
    dp[0][0] = 0
    for i in range(1, n+2):
        for j in range(1, k+1):
            for d in range(1, m+1):
                if i - d < 0: break
                dp[i][j] = max(dp[i][j], dp[i-d][j-1] + arr[i])
    print(max(dp[n+1]))