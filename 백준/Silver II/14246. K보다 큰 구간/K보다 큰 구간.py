import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
k = int(input())
for i in range(1, n):
    l[i] += l[i-1]
l.append(0)
i, j = 0, 0
ret = 0
while j < n:
    while j < n and l[j] - l[i-1] <= k:
        j += 1
    if j != n:
        ret += n-j
        i += 1
print(ret)