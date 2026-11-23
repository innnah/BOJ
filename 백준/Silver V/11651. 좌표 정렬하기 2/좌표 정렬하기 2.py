n = int(input())
xylist = [list(map(int, input().split()))[::-1] for _ in range(n)]
xylist.sort()

for x in xylist:
    print(x[1], x[0])