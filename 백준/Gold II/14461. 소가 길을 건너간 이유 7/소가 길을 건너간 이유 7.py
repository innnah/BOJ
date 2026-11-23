import sys, heapq
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
INF = 98765432123456789
def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y, 0))
    distance[y][x][0] = 0
    while q:
        _, x, y, cnt = heapq.heappop(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (1 <= nx <= n and 1 <= ny <= n): continue
            cost = distance[y][x][cnt] + t
            if cnt == 2: 
                cost += l[ny-1][nx-1]
            if cost < distance[ny][nx][(cnt+1)%3]:
                distance[ny][nx][(cnt+1)%3] = cost
                heapq.heappush(q, (cost, nx, ny, (cnt+1)%3))
n, t = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
distance = [[[INF] * 3 for _ in range(n+1)] for _ in range(n+1)]
dijkstra(1, 1)
print(min(distance[n][n]))