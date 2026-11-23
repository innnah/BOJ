a, b = 0, 0
for _ in range(int(input())):
    sa, sb = map(int, input().split())
    if sa > sb: a += 1
    elif sa < sb: b += 1
print(a, b)