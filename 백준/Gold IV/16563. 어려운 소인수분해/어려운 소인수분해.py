import sys

input = sys.stdin.readline
print = sys.stdout.write

def sieve2(n):
    sqrt = int(n**0.5)
    for i in range(2, n+1):
        minFactor[i] = i

    for j in range(2, sqrt+1):
        if minFactor[j] == j:
            for k in range(j*j, n+1, j):
                if minFactor[k] == k:
                    minFactor[k] = j

n = int(input())
l = list(map(int, input().split()))
m = max(l)
minFactor = [-1] * (m+1)
sieve2(m)
for i in l:
    ret = []
    num = i
    while num > 1:
        ret.append(str(minFactor[num]))
        num //= minFactor[num]
    print(' '.join(ret) + "\n")