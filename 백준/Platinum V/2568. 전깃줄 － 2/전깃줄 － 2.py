import sys
from bisect import bisect_left

input = sys.stdin.readline

cache = []
def lis(sequence):
    L = []
    for i in range(len(sequence)):
        s = bisect_left(L, sequence[i])
        if len(L) > s: 
            L[s] = sequence[i]
        else: 
            L.append(sequence[i])
        cache.append(s+1)
    return L

n = int(input())
l = sorted([list(map(int, input().split())) for _ in range(n)])
lis_l = lis([l[i][1] for i in range(n)])

print(n - len(lis_l))
size = len(lis_l)
cache2 = []
for i in range(len(cache)-1,-1,-1):
    if cache[i] == size:
        size -= 1
    else: 
        cache2.append(l[i][0])
for i in cache2[::-1]:
    print(i)