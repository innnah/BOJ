import sys
input = sys.stdin.readline

class Seg:
    def __init__(self, n, arr):
        self.tree = [0 for _ in range(n*4+8)]
        self.arr = arr
        self.makeTree(1, 0, n-1)
    def makeTree(self, v, s, e):
        if s == e:
            self.tree[v] = self.arr[s]
            return self.tree[v]
        mid = (s + e) // 2
        self.tree[v] = min(self.makeTree(v*2, s, mid), self.makeTree(v*2+1, mid+1, e))
        return self.tree[v]
    def query(self, l, r, v, s, e):
        if l <= s <= e <= r: return self.tree[v]
        if e < l or r < s: return 10**20
        mid = (s + e) // 2
        return min(self.query(l, r, v*2, s, mid), self.query(l, r, v*2+1, mid+1, e))

n, m = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(n)]
mx = Seg(n, [-tmp[i][0] for i in range(n)])
mn = Seg(n, [tmp[i][1] for i in range(n)])
p, q = 0, 0
ret = [-1, []]
while p < n:
    v1 = -mx.query(p, q, 1, 0, n-1)
    v2 = mn.query(p, q, 1, 0, n-1)
    if v2 < v1:
        p += 1
    else:
        if ret[0] < q-p+1:
            ret = [q-p+1, [[v1, v2]]]
        elif ret[0] == q-p+1:
            ret[1].append([v1, v2])
        q += 1
    if q >= n:
        break
ret[1].sort()
a = [ret[1][0].copy()]
for i in range(1, len(ret[1])):
    if a[-1][1] < ret[1][i][0]:
        a.append(ret[1][i].copy())
    else:
        a[-1][1] = max(ret[1][i][1], a[-1][1])
ans = 0
for i in a:
    ans += i[1] - i[0] + 1
print(ret[0], ans)