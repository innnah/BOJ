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
        self.tree[v] = min(self.makeTree(v*2, s, mid), self.makeTree(v*2+1, mid+1, e))
        return self.tree[v]
    def __query(self, v, s, e, l, r):
        if l > e or r < s: return 98765432123456789
        if l <= s <= e <= r: return self.tree[v]
        mid = (s + e) // 2
        return min(self.__query(v*2, s, mid, l, r), self.__query(v*2+1, mid+1, e, l, r))
    def query(self, l, r):
        return self.__query(1, 0, self.n-1, l, r)

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
minusl = [-i for i in l]
segmin = SegTree(l)
segmax = SegTree(minusl)
for _ in range(m):
    a, b = map(int, input().split())
    print(segmin.query(a-1, b-1), -segmax.query(a-1, b-1))