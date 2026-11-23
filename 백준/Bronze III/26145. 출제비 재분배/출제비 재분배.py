n, m = map(int, input().split())
l = list(map(int, input().split())) + [0 for _ in range(m)]
for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(1, n+m+1):
        l[i-1] -= a[j-1]
        l[j-1] += a[j-1]
print(*l)