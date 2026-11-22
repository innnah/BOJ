import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = 0
for i in range(n):
    if s+1 < arr[i]:
        print(s+1)
        break
    s += arr[i]
else:
    print(sum(arr)+1)