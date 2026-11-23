import sys
input = sys.stdin.readline

l = list(input().rstrip())
n = len(l)
cache = [[0] * n for _ in range(n)]
for i in range(n):
    idx1 = idx2 = i
    while idx1 >= 0 and idx2 < n and l[idx1] == l[idx2]:
        cache[idx1][idx2] = 1
        idx1 -= 1
        idx2 += 1
for i in range(n-1):
    idx1 = i
    idx2 = i+1
    while idx1 >= 0 and idx2 < n and l[idx1] == l[idx2]:
        cache[idx1][idx2] = 1
        idx1 -= 1
        idx2 += 1

cache2 = [987654321 for _ in range(n)]
cache2[0] = 1
for i in range(1, n):
    if cache[0][i] == 1: 
        cache2[i] = 1
        continue
    cache2[i] = cache2[i-1] + 1
    for j in range(1, i+1):
        if cache[j][i]:
            cache2[i] = min(cache2[i], cache2[j-1]+1)
print(cache2[n-1])