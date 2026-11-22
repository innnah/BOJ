import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr2 = [-1 for _ in range(n+1)]
for i in range(n):
    arr2[arr[i]] = i
ret = 0
for i in range(1, n):
    ret += arr2[i] > arr2[i+1]
print(ret)