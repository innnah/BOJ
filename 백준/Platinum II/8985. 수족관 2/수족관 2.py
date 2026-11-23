import sys, bisect
from collections import deque
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
lines = []
for i in range(1, n):
    if points[i][1] == points[i - 1][1]:
        lines.append([points[i - 1][0], points[i][0], points[i][1], 0])
lines.sort()

m = int(input())
for _ in range(m):
    x1, h, x2, _ = map(int, input().split())
    idx = bisect.bisect_left(lines, [x1, x2, h, 0])
    lines[idx][3] += 1

lines.sort(key=lambda x: (x[2], x[0], x[1]))

nodes = [[points[0][0], points[-1][0], 0, 0, 0]]
graph = [[]]
q = deque()
q.append(0)
i = 0
while i < len(lines):
    h = lines[i][2]
    nxt = i + 1
    while nxt < len(lines) and lines[nxt][2] == h:
        nxt += 1
    j = i
    for _ in range(len(q)):
        cur = q.popleft()
        l, r, _, _, _ = nodes[cur]
        nxt_j = j
        while nxt_j < nxt and lines[nxt_j][1] <= r:
            nodes[cur][4] += lines[nxt_j][3]
            nxt_j += 1
        if nxt_j == j:
            q.append(cur)
            continue
        nodes[cur][3] = h
        if lines[j][0] > l:
            nodes.append([l, lines[j][0], h, h, 0])
            q.append(len(nodes) - 1)
            graph.append([])
            graph[cur].append(len(nodes) - 1)
        while j < nxt_j - 1:
            nodes.append([lines[j][1], lines[j + 1][0], h, h, 0])
            q.append(len(nodes) - 1)
            graph.append([])
            graph[cur].append(len(nodes) - 1)
            j += 1
        if lines[j][1] < r:
            nodes.append([lines[j][1], r, h, h, 0])
            q.append(len(nodes) - 1)
            graph.append([])
            graph[cur].append(len(nodes) - 1)
        j += 1
    i = nxt

holes = [0 for _ in range(len(nodes))]
for i in range(len(nodes) - 1, -1, -1):
    holes[i] = nodes[i][4]
    for nxt in graph[i]:
        holes[i] += holes[nxt]

remain = 0
res = [0 for _ in range(len(nodes))]
for i in range(len(nodes) - 1, -1, -1):
    if holes[i] == 0:
        remain += (nodes[i][1] - nodes[i][0]) * (nodes[i][3] - nodes[i][2])
        continue
    t = (nodes[i][1] - nodes[i][0]) * (nodes[i][3] - nodes[i][2]) / holes[i]
    ret = 0
    for nxt in graph[i]:
        ret = max(ret, res[nxt])
    res[i] = ret + t
print(f"{res[0]:.2f}")
print(remain)