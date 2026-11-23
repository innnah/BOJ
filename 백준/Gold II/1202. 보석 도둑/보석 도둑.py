import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((b, a))
l.sort(key = lambda x : -x[1])
bags = [int(input()) for _ in range(m)]
bags.sort()
h = []
ret = 0
for i in range(m):
    while l and bags[i] >= l[-1][1]:
        heapq.heappush(h, -l.pop()[0])
    if h: ret += -heapq.heappop(h)
print(ret)