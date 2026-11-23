from bisect import bisect_left
import sys

input = sys.stdin.readline

def lis(sequence):
    L = [sequence[0]]
    for i in range(1, len(sequence)):
        if L[-1] < sequence[i]:
            L.append(sequence[i])
        else:
            lower_bound = bisect_left(L, sequence[i])
            L[lower_bound] = sequence[i]
    return len(L)

n = int(input())
l = list(map(int, input().split()))
print(lis(l))