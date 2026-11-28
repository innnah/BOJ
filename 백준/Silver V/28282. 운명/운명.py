import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt1 = [0 for _ in range(m+1)]
cnt2 = [0 for _ in range(m+1)]
for i in range(n):
    cnt1[arr[i]] += 1
for i in range(n, 2*n):
    cnt2[arr[i]] += 1

ret = 0
for i in range(1, m+1):
    ret += cnt1[i] * (n-cnt2[i])
print(ret)