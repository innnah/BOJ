import sys
input = sys.stdin.readline

MOD = 1000000007
class FenWickTree:
    def __init__(self, n):
        self.tree = [0 for _ in range(n+1)]
        self.n = n
    def query(self, v):
        ret = 0
        while v > 0:
            ret += self.tree[v]
            v -= (v & -v)
        return ret
    def update(self, idx, num):
        while idx <= self.n:
            self.tree[idx] += num
            idx += (idx & -idx)
n = int(input())
l = [int(input())+1 for _ in range(n)]
tree1 = FenWickTree(200002)
tree2 = FenWickTree(200002)
ret = 1
tree1.update(l[0], 1)
tree2.update(l[0], l[0])
for i in range(1, n):
    left = tree2.query(l[i])
    right = tree2.query(200002) - left
    mul = 2 * tree1.query(l[i]) - tree1.query(200002)
    ret = (ret * (right - left + l[i] * mul)) % MOD
    tree1.update(l[i], 1)
    tree2.update(l[i], l[i])
print(ret)