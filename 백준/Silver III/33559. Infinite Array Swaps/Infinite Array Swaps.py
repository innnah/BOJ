import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
d1 = defaultdict(int)
d2 = defaultdict(int)
for i in range(n):
    d1[arr1[i]] += 1
    d2[arr2[i]] += 1
ans1 = []
ans2 = []
cnt = 0
for i in d1.keys():
    v = min(d1[i], d2[i])
    cnt += v
    for j in range(v):
        ans1.append(i)
        ans2.append(i)
    d1[i] -= v
    d2[i] -= v
for i in d1.keys():
    for _ in range(d1[i]):
        ans1.append(i)
for i in d2.keys():
    for _ in range(d2[i]):
        ans2.append(i)
print(cnt)
print(*ans1)
print(*ans2)