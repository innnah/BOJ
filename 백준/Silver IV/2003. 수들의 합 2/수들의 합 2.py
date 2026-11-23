import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = list(map(int, input().split()))
b, e = 0, 0
s = 0
cnt = 0
while b < n:
    if s >= m:
        if s == m: cnt += 1
        s -= l[b]
        b += 1
    else:
        e += 1
        if e > n:
            break
        s += l[e-1]
print(cnt)