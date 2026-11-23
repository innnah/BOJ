numlist = list(map(int, input().split()))
ret = [min(numlist), max(numlist)]
numlist.remove(max(numlist))
ret.insert(1, max(numlist))

for x in ret:
    print(x, end = ' ')