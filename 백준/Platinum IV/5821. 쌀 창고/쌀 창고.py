import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
psum = [arr[0]]
for i in range(1, n):
    psum.append(psum[-1]+arr[i])
psum.append(0)
p, q = 0, 0
ret = 0
while p < n:
    mid = (p + q) // 2
    val = arr[mid] * (mid-p+1) - (psum[mid] - psum[p-1]) + (psum[q] - psum[mid-1]) - arr[mid] * (q-mid+1)
    if val <= k:
        ret = max(ret, q-p+1)
        q += 1
    else:
        p += 1
    if q >= n:
        break
print(ret)