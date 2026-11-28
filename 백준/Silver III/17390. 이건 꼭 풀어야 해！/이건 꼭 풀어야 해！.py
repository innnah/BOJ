import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
s = [0]
for i in range(n):
    s.append(s[i]+l[i])

for _ in range(k):
    start, end = map(int, input().split())
    print(s[end] - s[start-1])