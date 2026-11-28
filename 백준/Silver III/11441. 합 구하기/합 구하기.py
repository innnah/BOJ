import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[i]+l[i])

k = int(input())
for _ in range(k):
    start, end = map(int, input().split())
    print(s[end] - s[start-1])