import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
cnt = list(map(int, input().split()))
s = 0
for i in range(k):
    s += cnt[i]-1
    print(arr[s%(2*n)], end = ' ')