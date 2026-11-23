import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    heapq.heapify(l)
    ret = 0
    for i in range(n-1):
        a = heapq.heappop(l)
        b = heapq.heappop(l)
        ret += a + b
        heapq.heappush(l, a+b)
    print(ret)