import sys
input = sys.stdin.readline
n = int(input())
xylist = [list(map(int, input().split())) for _ in range(n)]

xylist.sort()

for i in xylist:
    for x in i:
        print(x, end = ' ')
    print()