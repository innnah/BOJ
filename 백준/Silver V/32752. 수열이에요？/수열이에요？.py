import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
arr[l-1:r] = sorted(arr[l-1:r])
print(int(sorted(arr) == arr))