import sys
input = sys.stdin.readline

def f(s, x):
    return psum[s+x-1]-psum[s-1] <= m

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
psum = [0 for _ in range(n+1)]
psum[0] = arr[0]
for i in range(1, n):
    psum[i] = psum[i-1] + arr[i]
r1 = [0 for _ in range(n+1)]
r2 = [0 for _ in range(n+1)]
s, e = 0, 0
while s < n:
    if e < n-1 and psum[e] - psum[s-1] <= m:
        e += 1
    else:
        r1[s] = e-s+1
        if psum[e] - psum[s-1] > m: r1[s] -= 1
        s += 1
s, e = n-1, n-1
while e >= 0:
    if s > 0 and psum[e] - psum[s-1] <= m:
        s -= 1
    else:
        r2[e] = e-s+1
        if psum[e] - psum[s-1] > m: r2[e] -= 1
        e -= 1
ans = [-1 for _ in range(n)]
for i in range(n):
    tmp = min(r2[i-1], r1[i])
    ans[i-tmp] = max(ans[i-tmp], tmp)
cur = ans[0]
print(max(0, cur)*2)
for i in range(1, n):
    cur -= 1
    cur = max(cur, ans[i])
    print(max(0, cur)*2)