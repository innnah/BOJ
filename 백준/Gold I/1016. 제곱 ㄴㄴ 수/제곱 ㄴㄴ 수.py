import math

n, m = map(int, input().split())
l = [1 for _ in range(m-n+1)]
i = 2
while i ** 2 <= m:
    mul = math.ceil(n / (i**2))
    while mul * (i**2) <= m:
        if mul * (i**2) >= 0:
            l[mul*(i**2)-n] = 0
        mul += 1
    i += 1

print(sum(l))