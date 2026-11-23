import sys
from heapq import heappop, heapify, heappush
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
heapify(l)
ret = 0
for i in range(n-1):
    a = heappop(l)
    b = heappop(l)
    ret += a + b
    heappush(l, a+b)
print(ret)