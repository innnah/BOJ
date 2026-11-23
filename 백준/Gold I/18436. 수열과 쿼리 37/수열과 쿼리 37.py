import sys
input = sys.stdin.readline
print = sys.stdout.write

class SegTree:
    def __init__(self, l):
        self.n = len(l)
        self.__arr = l
        self.tree = [(0, 0) for _ in range(self.n*4+1)]
        self.makeTree(1, 0, self.n-1)
    def makeTree(self, v, s, e):
        if s == e:
            self.tree[v] = (self.__arr[s] % 2, self.__arr[s] % 2 == 0)
            return self.tree[v]
        mid = (s + e) // 2
        left, right = self.makeTree(v*2, s, mid), self.makeTree(v*2+1, mid+1, e)
        self.tree[v] = (left[0] + right[0], left[1] + right[1])
        return self.tree[v]

    def __query(self, v, s, e, l, r):
        if l > e or r < s: return (0, 0)
        if l <= s and e <= r: return self.tree[v]
        mid = (s + e) // 2
        left, right = self.__query(v*2, s, mid, l, r), self.__query(v*2+1, mid+1, e, l, r)
        return left[0] + right[0], left[1] + right[1]
    def query(self, l, r):
        return self.__query(1, 0, self.n-1, l, r)
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return
        if self.__arr[idx] % 2 != val % 2:
            if val % 2:
                self.tree[v] = (self.tree[v][0] + 1, self.tree[v][1] - 1)
            else:
                self.tree[v] = (self.tree[v][0] - 1, self.tree[v][1] + 1)
        if s != e:
            mid = (s + e) // 2
            self.__update(v*2, s, mid, idx, val)
            self.__update(v*2+1, mid+1, e, idx, val)
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val)
        self.__arr[idx] = val

n = int(input())
l = list(map(int, input().split()))
seg = SegTree(l)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a-1:        
        ret = seg.query(b-1, c-1)
        print(f"{ret[not (a-2)]}\n")
    else:
        seg.update(b-1, c)