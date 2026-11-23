n = int(input())
numlist = [int(input()) for _ in range(n)]

numlist.sort()

for x in numlist:
    print(x)