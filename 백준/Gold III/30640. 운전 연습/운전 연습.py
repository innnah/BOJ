import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n+1)]
for i in range(n):
    arr[i][1] -= arr[i+1][0] - arr[i][0]
psum = [0 for _ in range(n+1)]
psum[0] = arr[0][1]
for i in range(1, n+1):
    psum[i] = psum[i-1] + arr[i][1]
flag = 0
start = 0
for i in range(1, n+1):
    if psum[i-1] < 0:
        flag = 1
    if flag:
        print(-1, -1)
        continue
    print(start, psum[i-1])
    if psum[i-1] == 0:
        start = i