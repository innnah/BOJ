import sys

sys.setrecursionlimit(2147483647)

n = int(input())
MOD = 10007
cache = [-1 for _ in range(1001)]

def tiling(n):
    if n <= 1: return 1
    ret = cache[n]
    if ret != -1: return ret
    cache[n] = (tiling(n-1) + tiling(n-2)*2) % MOD
    return cache[n]

print(tiling(n))