import sys
input = sys.stdin.readline

def find(u):
    if u != unionfind[u]: unionfind[u] = find(unionfind[u])
    return unionfind[u]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    unionfind[root2] = root1

n, m = map(int, input().split())
_, *truth = list(map(int, input().split()))
parties = []
unionfind = [i for i in range(n+1)]
for _ in range(m):
    _, *party = list(map(int, input().split()))
    parties.append(party)
    for i in range(1, len(party)): union(party[i-1], party[i])
ret = 0
for party in parties:
    tell_lie = True
    for t in truth:
        for p in party:
            if find(p) == find(t):
                tell_lie = False
                break
        if not tell_lie: break
    else: ret += 1
print(ret)