import sys

input = sys.stdin.readline

n = int(input())
numlist = list(set(map(int, input().split())))
numlist.sort()

for x in numlist:
    print(x, end = ' ')