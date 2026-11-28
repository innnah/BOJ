import sys
input = sys.stdin.readline

def query(val, v, s, e):
    if val < s or tree[v] > 0:
        return 987654321
    if s == e:
        return s
    mid = (s + e) // 2
    if e <= val:
        if tree[v*2+1] == 0:
            return query(val, v*2+1, mid+1, e)
        if tree[v*2] == 0:
            return query(val, v*2, s, mid)
        return 987654321
    v1 = query(val, v*2+1, mid+1, e)
    if v1 != 987654321: return v1
    return query(val, v*2, s, mid)
    
def update(idx, val, v, s, e):
    if idx < s or idx > e: return tree[v]
    if s == e: 
        tree[v] = val
        return tree[v]
    mid = (s + e) // 2
    tree[v] = min(update(idx, val, v*2, s, mid), update(idx, val, v*2+1, mid+1, e))
    return tree[v]

n = int(input())
m = int(input())
tree = [0 for _ in range(n*4+4)]
for i in range(m):
    k = int(input())
    v = query(k-1, 1, 0, n-1)
    if v == 987654321:
        print(i)
        break
    update(v, 1, 1, 0, n-1)
else:
    print(m)