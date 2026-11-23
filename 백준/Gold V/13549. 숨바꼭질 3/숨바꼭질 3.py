import heapq

INF = 987654321
moves = [-1, 1]
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in range(2):
            cost = distance[node] + 1
            ne = node + moves[i]
            if 0 <= ne <= 200000 and cost < distance[ne]:
                distance[ne] = cost
                heapq.heappush(q, (cost, ne))
        cost = distance[node]
        ne = node*2
        if 0 <= ne <= 200000 and cost < distance[ne]:
            distance[ne] = cost
            heapq.heappush(q, (cost, ne))

n, k = map(int, input().split())
distance = [INF for _ in range(200005)]
dijkstra(n)
print(distance[k])