def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    if int(n * multiplier * 10) % 10 < 5:
        return int(n * multiplier) / multiplier
    else:
        return (int(n * multiplier) + 1) / multiplier

n = int(input())
ret = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    m = tmp[0]
    numlist = tmp[1:]
    average = sum(numlist) / m
    percent = 0

    for x in numlist:
        if x > average:
            percent += (1 / m) * 100

    ret.append(truncate(percent, 3))

for x in ret:
    print("%0.3f%%" % x)