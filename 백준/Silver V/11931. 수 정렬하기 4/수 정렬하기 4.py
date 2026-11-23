import sys
input = sys.stdin.readline
n = int(input())
numlist = [int(input()) for _ in range(n)]
numlist.sort(reverse = True)

for x in numlist:
    print(x)