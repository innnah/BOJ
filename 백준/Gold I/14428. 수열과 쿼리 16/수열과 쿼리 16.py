import sys
input = sys.stdin.readline
print = sys.stdout.write

class SegTree:
    def __init__(self, l):
        self.n = len(l)
        self.__arr = l
        self.tree = [[0, 0] for _ in range(self.n*4+1)]
        self.makeTree(1, 0, self.n-1)
    def makeTree(self, v, s, e):
        if s == e:
            self.tree[v] = [self.__arr[s], s]
            return self.tree[v]
        mid = (s + e) // 2
        left = self.makeTree(v*2, s, mid)
        right = self.makeTree(v*2+1, mid+1, e)
        if left[0] <= right[0]:
            self.tree[v] = left
        else:
            self.tree[v] = right
        return self.tree[v]

    def __query(self, v, s, e, l, r):
        if l > e or r < s: return (98765432199, 98765432199)
        if l <= s <= e <= r: return self.tree[v]
        mid = (s + e) // 2
        left = self.__query(v*2, s, mid, l, r)
        right = self.__query(v*2+1, mid+1, e, l, r)
        if left[0] <= right[0]:
            return left
        else:
            return right
    def query(self, l, r):
        return self.__query(1, 0, self.n-1, l, r)
        
    def __update(self, v, s, e, idx, val):
        if idx < s or idx > e: return self.tree[v]
        if s == e: 
            self.tree[v][0] += val
            return self.tree[v]
        mid = (s + e) // 2
        left = self.__update(v*2, s, mid, idx, val)
        right = self.__update(v*2+1, mid+1, e, idx, val)
        if left[0] <= right[0]:
            self.tree[v] = left
        else:
            self.tree[v] = right
        return self.tree[v]
    def update(self, idx, val):
        self.__update(1, 0, self.n-1, idx, val - self.__arr[idx])
        self.__arr[idx] = val

n = int(input())
l = list(map(int, input().split()))
seg = SegTree(l)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a-1:
        print(f"{seg.query(b-1, c-1)[1]+1}\n")
    else:
        seg.update(b-1, c)