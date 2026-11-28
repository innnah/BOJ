import sys
input = sys.stdin.readline

def makeTree(v, s, e):
    if s == e:
        tree[v] = arr2[s]
        return tree[v]
    mid = (s + e) // 2
    tree[v] = makeTree(v*2, s, mid) + makeTree(v*2+1, mid+1, e)
    return tree[v]
def query(le, ri, v, s, e):
    if le > e or ri < s: return 0
    if le <= s <= e <= ri: return tree[v]
    mid = (s + e) // 2
    return query(le, ri, v*2, s, mid) + query(le, ri, v*2+1, mid+1, e)
def query2(k, v, s, e):
    if s == e:
        return se[s]
    mid = (s+e)//2
    if tree[v*2] < k:
        return query2(k-tree[v*2], v*2+1, mid+1, e)
    return query2(k, v*2, s, mid)
def update(idx, val, v, s, e):
    if idx < s or idx > e: return tree[v]
    if s == e: 
        tree[v] += val
        return tree[v]
    mid = (s + e) // 2
    tree[v] = update(idx, val, v*2, s, mid) + update(idx, val, v*2+1, mid+1, e)
    return tree[v]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
se = set(arr)
querys = [list(map(int, input().split())) for _ in range(m)]
tmp = arr.copy()
for i in range(m):
    if querys[i][0] == 1:
        a, b = querys[i][1], querys[i][2]
        tmp[a-1] += b
        se.add(tmp[a-1])
    if querys[i][0] == 2:
        a, b = querys[i][1], querys[i][2]
        tmp[a-1] -= b
        se.add(tmp[a-1])
    if querys[i][0] == 3:
        a, b = querys[i][1], querys[i][2]
        se.add(a)
        se.add(b)
d = {}
se = list(se)
se.sort()
d = {se[i] : i for i in range(len(se))}
tree = [0 for _ in range(len(se)*4+8)]
arr2 = [0 for _ in range(len(se))]
for i in arr:
    arr2[d[i]] += 1

makeTree(1, 0, len(se)-1)
for i in range(m):
    qn = querys[i][0]
    if qn == 1:
        a, b = querys[i][1], querys[i][2]
        update(d[arr[a-1]], -1, 1, 0, len(se)-1)
        arr[a-1] += b
        update(d[arr[a-1]], 1, 1, 0, len(se)-1)
    elif qn == 2:
        a, b = querys[i][1], querys[i][2]
        update(d[arr[a-1]], -1, 1, 0, len(se)-1)
        arr[a-1] -= b
        update(d[arr[a-1]], 1, 1, 0, len(se)-1)
    elif qn == 3:
        a, b = querys[i][1], querys[i][2]
        print(query(d[a], d[b], 1, 0, len(se)-1))
    else:
        a = querys[i][1]
        print(query2(n-a+1, 1, 0, len(se)-1))