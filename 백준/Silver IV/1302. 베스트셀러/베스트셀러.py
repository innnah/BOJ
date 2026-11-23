import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
d = defaultdict(int)
for _ in range(n):
    s = input().rstrip()
    d[s] += 1
l = list(d.items())
l.sort(key = lambda x:(-x[1], x[0]))
print(l[0][0])