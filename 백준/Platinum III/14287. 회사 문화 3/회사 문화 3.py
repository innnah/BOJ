import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

'''
void dfs(int v, int a)
{
    s[v] = ++cnt;
    for (int next : graph[v]) {
        if (next == a) continue;
        dfs(next, v);
    }
    e[v] = cnt;
}
'''
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
        if l <= s <= e <= r: return self.tree[v]
        mid = (s + e) // 2
        tmp = self.__query(v*2, s, mid, l, r) + self.__query(v*2+1, mid+1, e, l, r)
        return tmp
    def query(self, l, r):
        return self.__query(1, 0, self.n-1, l, r)
        
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
cnt = 0
def dfs(v, a):
    global cnt
    cnt += 1
    s[v] = cnt
    for next in graph[v]:
        if next == a: continue
        dfs(next, v)
    e[v] = cnt
n, m = map(int, input().split())
s = [0 for _ in range(n+1)]
e = [0 for _ in range(n+1)]
l = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(1, n):
    graph[l[i]].append(i+1)
dfs(1, -1)
seg = SegTree([0 for _ in range(n+1)])
for _ in range(m):
    a = list(map(int, input().split()))
    if a[0]-1:
        print(seg.query(s[a[1]], e[a[1]]))
    else:
        seg.update(s[a[1]], a[2])