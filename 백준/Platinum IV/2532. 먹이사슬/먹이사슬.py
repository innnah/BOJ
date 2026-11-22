import sys
input = sys.stdin.readline
from bisect import bisect

def lis(sequence):
    L = [sequence[0]]
    for i in range(1, len(sequence)):
        if L[-1] <= sequence[i]:
            L.append(sequence[i])
        else:
            lower_bound = bisect(L, sequence[i])
            L[lower_bound] = sequence[i]
    return len(L)

n = int(input())
l = list(set(tuple(map(int, input().split()))[1:] for _ in range(n)))
l.sort(key=lambda x:(x[0], -x[1]))
arr = [i[1] for i in l][::-1]
print(lis(arr))