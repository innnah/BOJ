import sys
input = sys.stdin.readline
sys.setrecursionlimit(987654321)
d = {}
n, p, q, x, y = map(int, input().split())
def solve(n):
    if n < 1: return 1
    if d.get(n)!=None: return d[n]
    d[n] = solve(n//p-x)+solve(n//q-y)
    return d[n]
print(solve(n))