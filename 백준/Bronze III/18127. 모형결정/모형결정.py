n, m = map(int, input().split())
a = 0
d = 1
for _ in range(m+1):
    a += d
    d += n-2
print(a)