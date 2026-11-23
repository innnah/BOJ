n, k, p = map(int, input().split())
s = 0
for c in range(1, n+1):
    s += k * c + p * c * c
print(s)