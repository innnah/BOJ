import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ret = 1
idx = 1
m = arr[0]
while 1:
    for j in range(idx, n):
        if arr[j] >= m:
            ret = max(ret, j-idx+1)
            idx = j+1
            m = arr[j]
            break
    else:
        print(max(ret, n-(idx-1)))
        sys.exit(0)