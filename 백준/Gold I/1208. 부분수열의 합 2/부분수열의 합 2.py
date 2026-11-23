import sys
from collections import defaultdict
input = sys.stdin.readline

def brute(num, size, idx, sum):
    if idx == size:
        s[num].append(sum)
        return
    brute(num, size, idx+1, sum)
    brute(num, size, idx+1, sum+arr[num][idx])

n, m = map(int, input().split())
l = list(map(int, input().split()))
arr = [[], []]
arr[0] = l[:n//2]
arr[1] = l[n//2:]
s = [[], []]
for i in range(2):
    brute(i, len(arr[i]), 0, 0)
d = defaultdict(int)
for i in s[1]:
    d[i] += 1
ret = 0
for i in s[0]:
    ret += d[m-i]
print(ret-(m==0))