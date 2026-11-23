import heapq, sys

input = sys.stdin.readline

l = []

n = int(input())
for _ in range(n):
    o = int(input())
    if o == 0:
        if l == []:
            print(0)
        else:
            print(l[0])
            heapq.heappop(l)
    else:
        heapq.heappush(l, o)