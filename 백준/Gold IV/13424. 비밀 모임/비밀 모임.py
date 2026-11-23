import sys, heapq

input = sys.stdin.readline

INF = 987654321
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        for ne in graph[node]:
            cost = distance[node] + ne[1]
            if cost < distance[ne[0]]:
                distance[ne[0]] = cost
                heapq.heappush(q, (cost, ne[0]))
for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    n = int(input())
    people = list(map(int, input().split()))
    dis_sum = [0 for _ in range(v)]
    for person in people:
        distance = [INF for _ in range(v+1)]
        dijkstra(person)
        for i in range(1, v+1):
            dis_sum[i-1] += distance[i]
    minnum = 0
    for i in range(v):
        if dis_sum[minnum] > dis_sum[i]:
            minnum = i
    print(minnum+1)