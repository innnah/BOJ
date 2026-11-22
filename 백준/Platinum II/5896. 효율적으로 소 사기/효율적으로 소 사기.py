import sys, heapq
input = sys.stdin.readline

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : [x[1], x[0]])
pq = []
ret = 0
for i in range(k):
    if arr[i][1] <= m:
        ret += 1
        heapq.heappush(pq, arr[i][0]-arr[i][1])
        m -= arr[i][1]
for i in range(k, n):
    if pq and pq[0] + arr[i][1] <= arr[i][0]:
        if pq[0] + arr[i][1] <= m:
            m -= pq[0] + arr[i][1]
            ret += 1
            heapq.heappop(pq)
            heapq.heappush(pq, arr[i][0]-arr[i][1])
    else:
        if arr[i][0] <= m:
            m -= arr[i][0]
            ret += 1
print(ret)