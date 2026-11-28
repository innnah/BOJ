import sys, bisect
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
want = [int(input()) for _ in range(n)]
for i in range(1, m):
    l[i] += l[i-1]
for i in want:
    idx = bisect.bisect_left(l, i)
    if idx == m:
        print("Go away!")
    else:
        print(idx+1)