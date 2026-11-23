from collections import defaultdict
d = defaultdict(int)
input()
l = list(map(int, input().split()))
cnt = 0
for i in l:
    d[i] += 1
    if d[i] > 1: cnt += 1
print(cnt)