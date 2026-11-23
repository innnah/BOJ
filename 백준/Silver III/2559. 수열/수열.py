n, m = map(int, input().split())
l = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[i]+l[i])

if m == 1:
    print(max(l))
elif m == n:
    print(sum(l))
else:
    start, end = 0, m
    maxvar = 0
    while end <= n:
        maxvar = max(maxvar, s[end] - s[start])
        start += 1
        end += 1
    print(maxvar)