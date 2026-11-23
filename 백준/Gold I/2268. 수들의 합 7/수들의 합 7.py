import sys
input = sys.stdin.readline

class SegTree:
    def __init__(self, l):
        self.n = len(l)
        self.__arr = l
        self.tree = [0 for _ in range(self.n*4+1)]
        self.makeTree(1, 0, self.n-1)
    def makeTree(self, v, s, e):
        if s == e:
            self.tree[v] = self.__arr[s]
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = self.makeTree(v*2, s, mid) + self.makeTree(v*2+1, mid+1, e)
        return self.tree[v]

    def __query(self, v, s, e, l, r):
        if l > e or r < s: return 0
        if l <= s and e <= r: return self.tree[v]
        mid = (s + e) // 2
        return self.__query(v*2, s, mid, l, r) + self.__query(v*2+1, mid+1, e, l, r)
    def query(self, l, r):
        if l > r: l, r = r, l
        return self.__query(1, 0, self.n-1, l, r)
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return
        self.tree[v] += val
        if s != e:
            mid = (s + e) // 2
            self.__update(v*2, s, mid, idx, val)
            self.__update(v*2+1, mid+1, e, idx, val)
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val - self.__arr[idx])
        self.__arr[idx] = val

n, k = map(int, input().split())
l = [0 for _ in range(n)]
seg = SegTree(l)
for _ in range(k):
    a, b, c = map(int, input().split())
    if a-1:
        print(seg.query(b-1, c-1))
    else:
        seg.update(b-1, c)