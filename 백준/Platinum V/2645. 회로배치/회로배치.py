import sys, heapq
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isInside(x, y): return 1<=x and x<=n and 1<=y and y<=n
def dijkstra():
    pq = [(1+(c-1)*(board[sy][sx]==1), sx, sy)]
    dist[sy][sx] = 1+(c-1)*(board[sy][sx]==1)
    while pq:
        d, x, y = heapq.heappop(pq)
        if y == -1: print(x, y, d)
        if dist[y][x] < d: continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isInside(nx, ny):
                if dist[y][x] + 1 + (c-1) * (board[ny][nx] == 1) < dist[ny][nx]:
                    dist[ny][nx] = dist[y][x] + 1 + (c-1) * (board[ny][nx] == 1)
                    trace[ny][nx] = [x, y]
                    heapq.heappush(pq, (dist[ny][nx], nx, ny))

n = int(input())
sx, sy, ex, ey = map(int, input().split())
c = int(input())
m = int(input())
circuits = [list(map(int, input().split())) for _ in range(m)]
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
for cir in circuits:
    s = cir[0]
    for i in range(1, len(cir)-2, 2):
        a = [cir[i], cir[i+1]]
        b = [cir[i+2], cir[i+3]]
        if a[0] == b[0]:
            for j in range(min(a[1], b[1]), max(a[1], b[1])+1):
                board[j][a[0]] = 1
        else:
            for j in range(min(a[0], b[0]), max(a[0], b[0])+1):
                board[a[1]][j] = 1
dist = [[98765432123456789 for _ in range(n+1)] for _ in range(n+1)]
trace = [[[-1, -1] for _ in range(n+1)] for _ in range(n+1)]
dijkstra()
print(dist[ey][ex])
x, y = ex, ey
t = [[ex, ey]]
while x != sx or y != sy:
    tmp = trace[y][x]
    t.append(tmp)
    x, y = tmp
t = t[::-1]
nt = [[sx, sy]]
for i in range(len(t)-1):
    if (nt[-1][0] == t[i][0]) ^ (t[i][0] == t[i+1][0]):
        nt.append(t[i])
nt.append([ex, ey])
if nt[0] == nt[1]:
    nt.pop(0)
print(len(nt), end = ' ')
for i in nt:
    print(*i, end = ' ')