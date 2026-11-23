import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
ret = 987654321
for i in range(n):
    ret = min(ret, n-l.count(l[i]))
for i in range(n):
    for j in range(i+1, n):
        a = [0 for _ in range(n)]
        gap = (l[j] - l[i]) / (j-i)
        if gap != int(gap): continue
        gap = int(gap)
        a[i] = l[i]
        for k in range(i-1, -1, -1):
            a[k] = a[k+1] - gap
        for k in range(i+1, n):
            a[k] = a[k-1] + gap
        cand = 0
        for k in range(n):
            if a[k] != l[k]: cand += 1
        ret = min(ret, cand)
print(ret)