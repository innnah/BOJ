import sys
input = sys.stdin.readline

class SegTree:
    def __init__(self, length):
        self.n = length
        self.tree = [0 for _ in range(self.n*4+1)]
        self.makeTree(1, 0, self.n-1)
    def makeTree(self, v, s, e):
        if s == e:
            self.tree[v] = 0
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = self.makeTree(v*2, s, mid) + self.makeTree(v*2+1, mid+1, e)
        return self.tree[v]
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return
        self.tree[v] += 1
        if s != e:
            mid = (s + e) // 2
            self.__update(v*2, s, mid, idx, val)
            self.__update(v*2+1, mid+1, e, idx, val)
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val)
    def __query(self, v, s, e, l, r):
        if l > e or r < s: return 0
        if l <= s <= e <= r: return self.tree[v]
        mid = (s + e) // 2
        return self.__query(v*2, s, mid, l, r) + self.__query(v*2+1, mid+1, e, l, r)
    def query(self, l, r):
        return self.__query(1, 0, self.n-1, l, r)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
h = [0 for _ in range(1000001)]
arr = [0 for _ in range(500001)]
for i in range(n):
    h[a[i]] = i
for i in range(n):
    arr[h[b[i]]] = i
seg = SegTree(n)
ret = 0
for i in range(n):
    ret += seg.query(arr[i], n-1)
    seg.update(arr[i], 1)
print(ret)