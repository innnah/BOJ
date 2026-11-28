import sys, heapq
input = sys.stdin.readline

n = int(input())
x = []
y = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    x.append([a, c, i])
    y.append([b, d, i])
x.sort()
y.sort()

ans = [[-1, -1] for _ in range(n)]
l = 0
pq = []
for i in range(1, n+1):
    while l < n and x[l][0] <= i:
        heapq.heappush(pq, [x[l][1], x[l][2]])
        l += 1
    if not pq or pq[0][0] < i:
        print("NIE")
        exit(0)
    t = heapq.heappop(pq)
    ans[t[1]][0] = i

l = 0
pq = []
for i in range(1, n+1):
    while l < n and y[l][0] <= i:
        heapq.heappush(pq, [y[l][1], y[l][2]])
        l += 1
    if not pq or pq[0][0] < i:
        print("NIE")
        exit(0)
    t = heapq.heappop(pq)
    ans[t[1]][1] = i

for i in range(n):
    print(*ans[i])