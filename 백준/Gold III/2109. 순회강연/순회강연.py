import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : -x[1])
pq = []
idx = 0
ret = 0
for i in range(10000, 0, -1):
    while idx < n and arr[idx][1] >= i:
        heapq.heappush(pq, [-arr[idx][0], -arr[idx][1]])
        idx += 1
    if pq:
        ret += -heapq.heappop(pq)[0]
print(ret)