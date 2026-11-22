import sys
input = sys.stdin.readline

while 1:
    n, m, k = map(int, input().split())
    if n == 0: break
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key = lambda x : abs(x[1]-x[2]))
    a, b = 0, 0
    ans = 0
    for i in range(n):
        if arr[i][1] < arr[i][2]:
            a += arr[i][0]
            ans += arr[i][1] * arr[i][0]
        else:
            b += arr[i][0]
            ans += arr[i][2] * arr[i][0]
    if a > m:
        idx = 0
        while a-m:
            if arr[idx][1] < arr[idx][2]:
                if arr[idx][0] <= a - m:
                    ans += arr[idx][0] * (arr[idx][2] - arr[idx][1])
                    a -= arr[idx][0]
                else:
                    ans += (a - m) * (arr[idx][2] - arr[idx][1])
                    a = m
            idx += 1
    if b > k:
        idx = 0
        while b-k:
            if arr[idx][1] >= arr[idx][2]:
                if arr[idx][0] <= b - k:
                    ans += arr[idx][0] * (arr[idx][1] - arr[idx][2])
                    b -= arr[idx][0]
                else:
                    ans += (b - k) * (arr[idx][1] - arr[idx][2])
                    b = k
            idx += 1
    print(ans)