import sys, heapq
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(1, n):
    graph[arr1[i-1]-1].append(i)

pq = [[arr[0], 0]]
ret = []
while pq:
    v = heapq.heappop(pq)
    ret.append(v[0])
    for i in graph[v[1]]:
        heapq.heappush(pq, [arr[i], i])
for i in ret:
    print(i)