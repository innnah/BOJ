import itertools

n, m = map(int, input().split())
numlist = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    sub = itertools.combinations(numlist, i)
    for x in sub:
        if sum(x) == m:
            cnt += 1

print(cnt)