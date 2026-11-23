n, d = map(int, input().split())
numlist = [str(i) for i in range(1, n + 1)]
cnt = 0

for x in numlist:
    cnt += x.count(str(d))

print(cnt)