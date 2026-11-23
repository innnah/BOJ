import fractions

def dfs(v, d):
    visited[v] = d
    for i in graph[v]:
        if visited[i[0]] == 0:
            dfs(i[0], d*i[1])
def gcd(a, b):
    while b != 0: a, b = b, a%b
    return a
def parse(f):
    f = str(f)
    idx = f.find("/")
    if idx != -1:
        return int(f[idx+1:])
    else:
        return 1
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c, d = map(int, input().split())
    rate = fractions.Fraction(d, c)
    revrate = fractions.Fraction(c,d)
    graph[a].append((b, rate))
    graph[b].append((a, revrate))
visited = [0 for _ in range(n)]
dfs(0, 1)
mul = parse(visited[0])
for i in range(1, n):
    tmp = parse(visited[i])
    mul = mul * tmp // gcd(tmp, mul)
for i in visited:
    print(int(i * mul), end = ' ')