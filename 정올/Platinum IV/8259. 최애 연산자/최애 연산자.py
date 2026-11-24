import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [arr[i]%m for i in range(n)]
    arr.sort()
    arr += [arr[i]+m for i in range(n)]
    psum = [0 for _ in range(2*n+1)]
    for i in range(n*2):
        psum[i] = psum[i-1] + arr[i]
    ans = 10**20
    for i in range(n):
        ans = min(ans, psum[i+n] - psum[i+n-n//2] - psum[i+n//2] + psum[i])
    print(ans)