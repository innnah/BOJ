import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))
    arr = [[t[i], b[i], a[i]] for i in range(n)]
    arr.sort()
    #print(arr)
    ans = 0
    for i in range(n-1):
        p, q = arr[i].copy(), arr[i+1].copy()
        if p[2] < q[2] and p[1] > q[1]:
            ans = max(ans, (q[2]-p[2])//(p[1]-q[1])+1)
        #print(ans)
    for i in range(n):
        arr[i][2] += arr[i][1]*ans
    for i in range(n-1):
        if arr[i][2] <= arr[i+1][2]:
            print(-1)
            break
    else:
        print(ans)