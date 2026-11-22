import sys
input = sys.stdin.readline

class SegTree:
    def __init__(self, n):
        self.tree = [0 for _ in range(n*4+8)]
    def query(self, k, v, s, e):
        if s == e:
            if self.tree[v] > k: return s-1
            return s
        mid = (s + e) // 2
        if self.tree[v*2] < k: return self.query(k-self.tree[v*2], v*2+1, mid+1, e)
        return self.query(k, v*2, s, mid)
    def query2(self, l, r, v, s, e):
        if e < l or r < s: return 0
        if l <= s <= e <= r: return self.tree[v]
        mid = (s + e) // 2
        return self.query2(l, r, v*2, s, mid) + self.query2(l, r, v*2+1, mid+1, e)
    def update(self, idx, val, v, s, e):
        if idx < s or idx > e: return self.tree[v]
        if s == e: 
            self.tree[v] += val
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = self.update(idx, val, v*2, s, mid) + self.update(idx, val, v*2+1, mid+1, e)
        return self.tree[v]
    
n, c = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(n)]
tmp.sort()
d = {tmp[i][0] : i for i in range(n)}
tmp = [[d[tmp[i][0]], tmp[i][1], tmp[i][2]] for i in range(n)]
tmp.sort(key = lambda x : x[1])
d = {tmp[i][1] : i for i in range(n)}
arr = [[tmp[i][0], d[tmp[i][1]], tmp[i][2]] for i in range(n)]
arr.sort()

seg1 = SegTree(n)
seg2 = SegTree(n)

idx = 0
ret = 0
while idx < n:
    st = arr[idx][0]
    while idx < n and arr[idx][0] == st:
        seg1.update(arr[idx][1], 1, 1, 0, n-1)
        seg2.update(arr[idx][1], arr[idx][2], 1, 0, n-1)
        idx += 1
    ret = max(ret, seg2.query2(0, seg1.query(c, 1, 0, n-1), 1, 0, n-1))
print(ret)