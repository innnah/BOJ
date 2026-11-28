import sys, bisect
input = sys.stdin.readline

def makeTree(v, s, e):
    if s == e:
        tree[v] = [l[s]]
        return tree[v]
    mid = (s + e) // 2
    left, right = makeTree(v*2, s, mid), makeTree(v*2+1, mid+1, e)
    idxA, idxB = 0, 0
    while idxA < len(left) or idxB < len(right):
        if idxA == len(left):
            tree[v].append(right[idxB])
            idxB += 1
        elif idxB == len(right):
            tree[v].append(left[idxA])
            idxA += 1
        else:
            if left[idxA] <= right[idxB]:
                tree[v].append(left[idxA])
                idxA += 1
            else:
                tree[v].append(right[idxB])
                idxB += 1
    return tree[v]
def query(le, ri, k, v, s, e):
    if le > e or ri < s: return 0
    if le <= s <= e <= ri:
        idx = bisect.bisect(tree[v], k)
        return len(tree[v])-idx
    mid = (s + e) // 2
    return query(le, ri, k, v*2, s, mid) + query(le, ri, k, v*2+1, mid+1, e)

n = int(input())
l = list(map(int, input().split()))
tree = [[] for _ in range(4*n+5)]
makeTree(1, 0, n-1)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(query(a-1, b-1, c, 1, 0, n-1))