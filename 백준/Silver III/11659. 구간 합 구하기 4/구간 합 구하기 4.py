import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = list(map(int, input().split()))
psum = [0]
for i in range(n):
    psum.append(psum[-1]+l[i])
for _ in range(m):
    a, b = map(int, input().split())
    print(psum[b]-psum[a-1])