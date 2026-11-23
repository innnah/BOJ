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

    def __query(self, v, s, e, no):
        if s == e: return s
        mid = (s + e) // 2
        if no > self.tree[v*2]: return self.__query(v*2+1, mid+1, e, no-self.tree[v*2])
        return self.__query(v*2, s, mid, no)
    def query(self, no):
        return self.__query(1, 0, self.n-1, no)
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return
        self.tree[v] += val
        if s != e:
            mid = (s + e) // 2
            self.__update(v*2, s, mid, idx, val)
            self.__update(v*2+1, mid+1, e, idx, val)
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val)

n = int(input())
l = list(map(int, input().split()))
seg = SegTree(l)
m = int(input())
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0]-1:
        print(seg.query(q[1])+1)
    else:
        seg.update(q[1]-1, q[2])