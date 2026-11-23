import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(v=1):
    sheeps = islands[v][1] * (islands[v][0] == 'S')
    for i in tree[v]:
        sheeps += dfs(i)
    return max(0, sheeps-islands[v][1] * (islands[v][0] == 'W'))

n = int(input())
tree = [[] for _ in range(n+1)]
islands = [[], ['S', 0]]
for i in range(2, n+1):
    tmp = input().rstrip().split()
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    tree[tmp[2]].append(i)
    islands.append(tmp)
print(dfs())