import sys
from bisect import bisect

input = sys.stdin.readline

def lis(sequence):
    L = [sequence[0][1]]
    for i in range(1, len(sequence)):
        if L[-1] <= sequence[i][1]:
            L.append(sequence[i][1])
        else:
            lower_bound = bisect(L, sequence[i][1])
            L[lower_bound] = sequence[i][1]
    return len(L)
p, q = map(int, input().split())
n = int(input())
l = []
for _ in range(n):
    i = list(map(int, input().split()))
    if 0 <= i[0] <= p and 0 <= i[1] <= q:
        l.append(i)
l.sort()
print(lis(l))