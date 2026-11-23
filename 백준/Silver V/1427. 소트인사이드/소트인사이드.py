numlist = list(map(int, list(input())))
numlist.sort(reverse = True)

for x in numlist:
    print(x, end = '')