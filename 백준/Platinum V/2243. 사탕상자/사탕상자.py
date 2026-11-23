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

    def __query(self, v, s, e, q):
        if s == e: return s
        mid = (s + e) // 2
        if self.tree[v*2] < q:
            return self.__query(v*2+1, mid+1, e, q-self.tree[v*2])
        return self.__query(v*2, s, mid, q)
    def query(self, q):
        return self.__query(1, 0, self.n-1, q)
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return self.tree[v]
        if s == e: 
            self.tree[v] += val
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = self.__update(v*2, s, mid, idx, val) + self.__update(v*2+1, mid+1, e, idx, val)
        return self.tree[v]
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val)

seg = SegTree([0 for _ in range(1000001)])
for _ in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        tmp = seg.query(query[1])
        print(tmp)
        seg.update(tmp, -1)
    else:
        seg.update(query[1], query[2])