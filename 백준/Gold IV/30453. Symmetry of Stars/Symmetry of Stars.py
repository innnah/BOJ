import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d = defaultdict(int)
for i in range(n):
    for j in range(n):
        mid = ((arr[i][0]+arr[j][0])/2, (arr[i][1]+arr[j][1])/2)
        d[mid] += 1
print(max(d.values()))