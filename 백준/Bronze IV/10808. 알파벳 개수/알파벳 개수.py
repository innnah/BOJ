import sys
from collections import defaultdict
input = sys.stdin.readline
n = input().rstrip()
d = defaultdict(int)
for i in n:
    d[i] += 1
for i in range(ord('a'), ord('z')+1):
    print(d[chr(i)], end = ' ')