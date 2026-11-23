import sys

n = list(input().rstrip())
intList = [int(i) for i in n]

if not (0 in intList) or sum(intList) % 3 != 0:
    print(-1)
    sys.exit(0)

intList.sort(reverse = True)

for x in intList:
    print(x, end = '')