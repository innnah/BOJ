import sys, heapq
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
for i in l:
    if i[0] > i[1]:
        i[0], i[1] = i[1], i[0]
k = int(input())
l.sort(key = lambda x : (x[1], x[0]))
ret = 0
pq = []
for i in range(n):
    lim = l[i][1] - k
    while pq and pq[0][0] < lim:
        heapq.heappop(pq)
    if l[i][1] - l[i][0] > k: continue
    heapq.heappush(pq, l[i])
    ret = max(ret, len(pq))
print(ret)