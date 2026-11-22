import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
k = l[0]
cnt = 1
for i in range(1, n):
    if k > l[i]:
        k = l[i]
    else:
        k = l[i]
        cnt += 1
print(cnt)