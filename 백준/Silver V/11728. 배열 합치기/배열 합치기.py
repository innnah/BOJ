import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numlist = []
for _ in range(2):
    tmp = list(map(int, input().split()))
    numlist += tmp
numlist.sort()

for x in numlist:
    print(x, end = ' ')