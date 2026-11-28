import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
arr = list(map(int, input().split()))
p = []
for i in range(n-1):
    width = arr[i+1] - arr[i]
    height = h - (w*h) / (arr[i+1]-arr[i]+w)
    p.append(width * height / 2)
for i in range(1, n-1):
    p[i] += p[i-1]
p.append(0)
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ans = w*h
    ans -= arr[l] * h / 2 + (w-arr[r]) * h / 2
    ans -= p[r-1] - p[l-1]
    print(ans)