import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m, k, d = map(int, input().split())
    a = n*m*(m-1)//2
    b = n*(n-1)*m*m//2
    t = a*k+b
    if t > d: print(-1)
    else: print(t*(d//t))