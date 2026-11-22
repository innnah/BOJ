import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def topology_sort():
    ret = []
    q = deque()
    for i in allchars:
        if indegree[i] == 0:
            q.append(i)
    while q:
        if len(q) > 1:
            print("?")
            sys.exit(0)
        v = q.popleft()
        ret.append(v)
        for i in graph[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    if len(allchars) != len(ret):
        print("!")
        sys.exit(0)
    return ret

n = int(input())
words = [input().rstrip() for _ in range(n)]
allchars = set()
for i in words:
    for char in i:
        allchars.add(char)
graph = defaultdict(set)
indegree = defaultdict(int)
for i in range(n):
    for j in range(i+1, n):
        for k in range(min(len(words[i]), len(words[j]))):
            if words[i][k] != words[j][k]:
                graph[words[i][k]].add(words[j][k])
                break
        else:
            if len(words[i]) > len(words[j]):
                print("!")
                sys.exit(0)
for i in graph.keys():
    for j in graph[i]:
        indegree[j] += 1
print(''.join(topology_sort()))