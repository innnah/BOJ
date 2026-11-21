import sys, bisect
input = sys.stdin.readline

def makeTree(v, s, e):
    if s == e:
        tree[v] = [arr[s]]
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
def query(v, s, e, k):
    if s == e:
        return s
    mid = (s+e)//2
    left = bisect.bisect_left(tree[v*2], a)
    right = bisect.bisect(tree[v*2], b)
    cnt = right-left
    if cnt+k >= c:
        return query(v*2, s, mid, k)
    else:
        return query(v*2+1, mid+1, e, k+cnt)

n, m = map(int, input().split())
tmp = list(map(int, input().split()))
e = list(sorted(tmp))
d = {e[i] : i for i in range(n)}
b = [d[i] for i in tmp]
arr = [0 for _ in range(n)]
for i in range(n):
    arr[b[i]] = i
tree = [[] for _ in range(4*n+4)]
makeTree(1, 0, n-1)
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    print(e[query(1, 0, n-1, 0)])