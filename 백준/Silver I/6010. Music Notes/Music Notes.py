import sys, bisect
input = sys.stdin.readline

n, q = map(int, input().split())
l = [int(input()) for _ in range(n)]
for i in range(1, n):
    l[i] += l[i-1]
for _ in range(q):
    print(bisect.bisect(l, int(input()))+1)