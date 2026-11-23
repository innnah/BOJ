import sys
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(int)
n = int(input())
for _ in range(n):
    a, b = input().rstrip().split()
    b = int(b)
    d[a] += b
l = list(d.values())
for i in l:
    if i == 5:
        print("YES")
        break
else:
    print("NO")