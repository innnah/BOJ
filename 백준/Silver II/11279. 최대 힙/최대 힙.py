import heapq
import sys

input = sys.stdin.readline

n = int(input())
maxheap = []

for _ in range(n):
    o = int(input())
    if o == 0:
        if maxheap == []:
            print(0)
        else:
            max_item = heapq.heappop(maxheap)[1]
            print(max_item)
    else:
        heapq.heappush(maxheap, (-o, o))