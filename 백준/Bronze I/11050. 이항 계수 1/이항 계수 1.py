cache = [[-1 for _ in range(20)] for _ in range(20)]

def bino(n, r):
    global cache
    if r == 0 or n == r: return 1
    if cache[n][r] == -1: cache[n][r] = bino(n - 1, r - 1) + bino(n - 1, r)
    return cache[n][r]

n, k = map(int, input().split())
print(bino(n, k))