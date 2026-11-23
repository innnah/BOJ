import sys
input = sys.stdin.readline

NEGINF = -float('inf')
INF = -NEGINF
def bellman_ford(start):
    dist[start] = earn[start]
    for k in range(n+60):
        for i in range(n):
            if dist[i] == NEGINF:
                continue
            for j, d in graph[i]:
                if dist[i]-d+earn[j] > dist[j]:
                    dist[j] = dist[i]+earn[j]-d
                    if k >= n-1: dist[j] = INF

n, s, e, m = map(int, input().split())
graph = [[] for _ in range(n)]
dist = [NEGINF for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
earn = list(map(int, input().split()))
bellman_ford(s)
if dist[e] >= INF:
    print("Gee")
elif dist[e] <= NEGINF:
    print("gg")
else:
    print(dist[e])