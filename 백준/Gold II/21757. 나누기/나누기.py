import sys

input = sys.stdin.readline
sys.setrecursionlimit(2147483647)

def divide(idx=0, cnt=0):
    if cnt == 3:
        if idx < n:
            return 1
        return 0
    if idx == n:
        return 0
    if cache[idx][cnt] != -1:
        return cache[idx][cnt]
    cache[idx][cnt] = 0
    if psum[idx+1] == (cnt+1) * k:
        cache[idx][cnt] += divide(idx+1, cnt+1)
    cache[idx][cnt] += divide(idx+1, cnt)

    return cache[idx][cnt]

n = int(input())
l = list(map(int, input().split()))
if sum(l) % 4 != 0:
    print(0)
    sys.exit(0)
psum = [0] * (n+1)
for i in range(1, n+1):
    psum[i] = psum[i-1] + l[i-1]
k = psum[-1] // 4
cache = [[-1 for _ in range(4)] for _ in range(n)]
print(divide())