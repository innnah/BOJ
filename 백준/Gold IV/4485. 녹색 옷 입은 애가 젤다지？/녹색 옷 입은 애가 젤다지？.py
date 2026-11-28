import sys, heapq

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
INF = 987654321
def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while q:
        dist, y, x = heapq.heappop(q)
        if x == n-1 and y == n-1:
            print(f"Problem {tc}: {dist}")
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = distance[y][x] + graph[ny][nx]
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))

tc = 1
while True:
    n = int(input())
    if n == 0: break
    distance = [[INF] * n for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]
    dijkstra()
    tc += 1