import sys
input = sys.stdin.readline

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : [x[0], x[1], -x[2], -x[3]])
ret = 0
idx = 0
prev = [3, 1]
while prev < [12, 1]:
    tmp = [-1, -1]
    while idx < n and [arr[idx][0], arr[idx][1]] <= prev:
        tmp = max(tmp, [arr[idx][2], arr[idx][3]])
        idx += 1
    prev = tmp.copy()
    if tmp == [-1, -1]:
        print(0)
        sys.exit(0)
    ret += 1
if prev < [12, 1]:
    print(0)
else:
    print(ret)