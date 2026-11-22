import sys
sys.setrecursionlimit(100000)
def solve(idx, weight):
    if idx == n:
        if weight >= 0: weights[weight] = 0
        return
    solve(idx+1, weight+l[idx])
    solve(idx+1, weight-l[idx])
    solve(idx+1, weight)

n = int(input())
l = list(map(int, input().split()))
weights = [1 for _ in range(sum(l)+1)]
solve(0, 0)
print(weights.count(1))