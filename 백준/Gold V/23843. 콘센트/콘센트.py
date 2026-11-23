import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
h = []  
l.sort(reverse=True)
for i in l:
    if len(h) < m: heapq.heappush(h, i)
    else: heapq.heappush(h, heapq.heappop(h)+i)
print(max(h))