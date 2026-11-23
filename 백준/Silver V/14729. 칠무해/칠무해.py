import sys

input = sys.stdin.readline

n = int(input())
numlist = [float(input()) for _ in range(n)]
numlist.sort()

for x in numlist[:7]:
    print("%.3f" % x)