n, x = map(int, input().split())
numlist = list(map(int, input().split()))

for a in numlist:
    if a < x:
        print(a, end = ' ')