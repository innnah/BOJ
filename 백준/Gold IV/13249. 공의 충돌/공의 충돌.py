import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
t = int(input())
ans = 0
for dir in range(2**n):
    left = []
    right = []
    for i in range(n):
        if dir & (1 << i): left.append(arr[i])
        else: right.append(arr[i])
    cnt = 0
    for i in range(len(left)):
        for j in range(len(right)):
            if 0 <= right[j] - left[i] <= t*2:
                cnt += 1
    ans += cnt
print(ans / (2**n))