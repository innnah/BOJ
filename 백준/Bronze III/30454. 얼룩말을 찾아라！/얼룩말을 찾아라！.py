import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maxval = 0
maxcnt = 0
for _ in range(n):
    s = list(map(int, input().rstrip()))
    cnt = 0
    for i in range(1, m):
        if s[i-1] == 1 and s[i] == 0:
            cnt += 1
    if s[-1] == 1:
        cnt += 1
    if maxval < cnt:
        maxval = cnt
        maxcnt = 1
    elif maxval == cnt:
        maxcnt += 1
print(maxval, maxcnt)