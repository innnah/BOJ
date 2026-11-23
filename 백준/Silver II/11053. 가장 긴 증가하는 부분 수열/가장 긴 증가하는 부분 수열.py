import sys
input = sys.stdin.readline
def lis2(l):
    cache = [1 for _ in range(n)]
    maxi = 1
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if l[i] < l[j]:
                cache[i] = max(cache[i], cache[j]+1)
        maxi = max(maxi, cache[i])
    return maxi

n = int(input())
l = list(map(int, input().split()))
print(lis2(l))