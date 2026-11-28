s = 0
for _ in range(int(input())):
    a, d, g = map(int, input().split())
    if a == d+g:
        s = max(s, a*(d+g)*2)
    else:
        s = max(s, a*(d+g))
print(s)