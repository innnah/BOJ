import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
ret = 9876543212123123
idx = 0
cand = 0
for i in range(n):
    if l[i] % 2:
        cand += i-idx
        idx += 1
ret = min(ret, cand)
idx, cand = 0, 0
for i in range(n):
    if l[i] % 2 == 0:
        cand += i-idx
        idx += 1
ret = min(ret, cand)
print(ret)