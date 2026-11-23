m = 0
c = 0
for _ in range(10):
    a, b = map(int, input().split())
    c += b-a
    m = max(m, c)
print(m)