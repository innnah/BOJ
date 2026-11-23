import sys, heapq
input = sys.stdin.readline

INF = 987654321
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 0, 0, start))
    distance[start] = (0, 0)
    while q:
        dist, a, b, node = heapq.heappop(q)
        for ne in range(len(graph1[node])):
            nnode = graph1[node][ne][0]
            ca, cb = (a + graph1[node][ne][1]), (b + graph2[node][ne][1])
            if not (ca > distance[nnode][0] and cb > distance[nnode][1]):
                if ca * cb < distance[nnode][0] * distance[nnode][1]:
                    distance[nnode] = (ca, cb)
                heapq.heappush(q, (ca * cb, ca, cb, nnode))
n = int(input())
graph1 = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]
distance = [(INF, INF) for _ in range(n)]
for i in range(n):
    a = input().rstrip()
    for j in range(n):
        if a[j] != '.':
            graph1[i].append((j, int(a[j])))
for i in range(n):
    a = input().rstrip()
    for j in range(n):
        if a[j] != '.':
            graph2[i].append((j, int(a[j])))
dijkstra(0)
if distance[1] == (INF, INF): print(-1)
else: print(distance[1][0] * distance[1][1])