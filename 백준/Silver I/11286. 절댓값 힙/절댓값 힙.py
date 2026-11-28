import sys, heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    i = int(input())
    if i != 0:
        heapq.heappush(heap, (abs(i), i))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)