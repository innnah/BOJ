import sys
input = sys.stdin.readline

def dfs(v, code):
    dna[v] = code
    for i in graph[v]:
        if dna[i] == -1:
            dfs(i, code)

n = int(input())
gender = [0 if input().rstrip() == "M" else 1 for _ in range(n)]
dna = [-1 for _ in range(n)]
alive = [1 for _ in range(n)]
graph = [[] for _ in range(n)]
m = int(input())
for _ in range(m):
    event = input().rstrip().split()
    if len(event) == 1:
        d = -int(event[0])
        d -= 1
        alive[d] = 0
    else:
        event[0] = int(event[0])
        event[1] = int(event[1])
        event[0] -= 1; event[1] -= 1
        if event[2] == 'M': event[2] = 0
        else: event[2] = 1
        gender.append(event[2])
        dna.append(-1)
        alive.append(1)
        graph.append([event[1]])
        graph[event[1]].append(len(dna)-1)
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    dfs(a-1, b)

cnt = 1
for i in range(len(graph)):
    if dna[i] == -1:
        dfs(i, cnt + 10**9)
        cnt += 1

codes = []
no_data = []
two = 0
for i in range(len(dna)):
    if alive[i]:
        if dna[i] > 10**9:
            if no_data and no_data[-1] != dna[i]:
                two = 1
            no_data.append(dna[i])
        else:
            if codes and codes[-1] != dna[i]:
                print("NO")
                exit(0)
            else:
                codes.append(dna[i])
if no_data:
    if two:
        print("POSSIBLY")
    else:
        if codes:
            print("POSSIBLY")
        else:
            print("YES")
else:
    print("YES")