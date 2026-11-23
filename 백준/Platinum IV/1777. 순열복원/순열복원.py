import sys
input = sys.stdin.readline

class SegTree:
    def __init__(self, l):
        self.n = len(l)
        self.arr = l
        self.tree = [0 for _ in range(self.n*4+1)]
        self.makeTree(1, 0, self.n-1)
    def makeTree(self, v, s, e):
        if s == e:
            self.tree[v] = (self.arr[s] == 0)
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = self.makeTree(v*2, s, mid) + self.makeTree(v*2+1, mid+1, e)
        return self.tree[v]
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return
        self.tree[v] -= 1
        if s != e:
            mid = (s + e) // 2
            self.__update(v*2, s, mid, idx, val)
            self.__update(v*2+1, mid+1, e, idx, val)
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val)
        self.arr[idx] = val
    def __search(self, v, s, e, val):
        if s == e: return s
        mid = (s+e)//2
        if self.tree[v*2+1] > val:
            return self.__search(v*2+1, mid+1, e, val)
        else:
            return self.__search(v*2, s, mid, val-self.tree[v*2+1])
    def search(self, val):
        return self.__search(1, 0, self.n-1, val)

n = int(input())
l = list(map(int, input().split()))
seg = SegTree([0 for _ in range(n)])
for i in range(n-1, -1, -1):
    seg.update(seg.search(l[i]), i+1)
print(*seg.arr)