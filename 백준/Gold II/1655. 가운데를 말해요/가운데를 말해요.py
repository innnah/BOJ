import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
lq, rq = [], []
push = 0
for _ in range(n):
    a = int(input())
    if push:
        heappush(rq, a)
    else:
        heappush(lq, (-a, a))
    push = not push
    if rq and lq:
        if lq[0][1] > rq[0]:
            v1, v2 = heappop(lq), heappop(rq)
            heappush(lq, (-v2, v2))
            heappush(rq, v1[1])
    if push:
        print(lq[0][1])
    else:
        print(min(lq[0][1], rq[0]))