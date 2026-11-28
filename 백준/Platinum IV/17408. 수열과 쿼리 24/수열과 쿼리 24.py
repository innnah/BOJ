import sys
input = sys.stdin.readline

def findMAX(a, b):
    l = list(sorted([a[0], a[1], b[0], b[1]]))
    return (l[-1], l[-2])

class SegTree:
    def __init__(self, l):
        self.n = len(l)
        self.__arr = l
        self.tree = [(0, 0) for _ in range(self.n*4+1)]
        self.makeTree(1, 0, self.n-1)
    def makeTree(self, v, s, e):
        if s == e:
            self.tree[v] = (0, self.__arr[s])
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = findMAX(self.makeTree(v*2, s, mid), self.makeTree(v*2+1, mid+1, e))
        return self.tree[v]

    def __query(self, v, s, e, l, r):
        if l > e or r < s: return (0, 0)
        if l <= s <= e <= r: return self.tree[v]
        mid = (s + e) // 2
        return findMAX(self.__query(v*2, s, mid, l, r), self.__query(v*2+1, mid+1, e, l, r))
    def query(self, l, r):
        return self.__query(1, 0, self.n-1, l, r)
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return self.tree[v]
        if s == e:
            self.tree[v] = (val, 0)
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = findMAX(self.__update(v*2, s, mid, idx, val), self.__update(v*2+1, mid+1, e, idx, val))
        return self.tree[v]
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val)
        self.__arr[idx] = val

n = int(input())
l = list(map(int, input().split()))
seg = SegTree(l)
m = int(input())
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0]-1:
        print(sum(seg.query(q[1]-1, q[2]-1)))
    else:
        seg.update(q[1]-1, q[2])