n, k = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()

print(numlist[k-1])