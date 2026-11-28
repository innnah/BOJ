import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

nums = [[] for _ in range(n+1)]
for i in range(n):
    nums[arr[i]].append(i)

cnt = [0 for _ in range(n+1)]
nums_sort = [0 for _ in range(n)]
for i in range(n):
    nums_sort[i] = nums_sort[i-1] + (cnt[arr[i]] == 0)
    cnt[arr[i]] += 1

moos = 0
for i in range(n):
    if len(nums[i]) >= 2:
        moos += nums_sort[nums[i][-2] - 1] - (len(nums[i]) >= 3)

print(moos)