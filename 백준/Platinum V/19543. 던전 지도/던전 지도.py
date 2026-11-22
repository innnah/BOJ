import sys, bisect
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [input().rstrip() for _ in range(k)]
u = [[-1] for _ in range(k)]
for i in range(k):
    for j in range(m):
        if arr[i][j] == 'U':
            u[i].append(j)
s = list(input().rstrip())
s = [ord(i)-65 for i in s]
a, b = 0, m-1
for i in range(m-2, -1, -1):
    if arr[s[-1]][i] == 'U':
        a = i+1
        break
res = b-a+1
for i in range(n-2, -1, -1):
    idx1 = bisect.bisect_left(u[s[i]], a)
    idx2 = bisect.bisect(u[s[i]], b) - 1
    a = u[s[i]][idx1-1]+1
    b = u[s[i]][idx2]
    res += b-a+1
print(res)