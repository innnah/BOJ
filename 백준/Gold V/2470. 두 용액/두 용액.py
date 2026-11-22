import sys, bisect
input = sys.stdin.readline

n = int(input())
l = list(sorted(map(int, input().split())))
ret = (-98765432123456780, 0)
sub = abs(ret[1] + ret[0])
for i in range(n):
    idx = bisect.bisect(l, -l[i])
    if 0 <= idx < n and idx != i:
        if sub > abs(l[i] + l[idx]):
            sub = abs(l[i] + l[idx])
            ret = (min(l[i], l[idx]), max(l[i], l[idx]))
    if 0 <= idx-1 < n and idx-1 != i:
        idx -= 1
        if sub > abs(l[i] + l[idx]):
            sub = abs(l[i] + l[idx])
            ret = (min(l[i], l[idx]), max(l[i], l[idx]))
print(*ret)