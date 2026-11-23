n = int(input())
numlist = [list(map(int, input().split())) for _ in range(n)]

for x in numlist:
    top = 1
    for y in numlist:
        if x == y:
            continue
        if x[0] < y[0] and x[1] < y[1]:
            top += 1
            
    print(top, end = ' ')