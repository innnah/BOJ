n = int(input())
numlist = list(map(int, input().split()))
nums = list(sorted(set(numlist)))
nums = {nums[i]:i for i in range(len(nums))}
print(*[nums[x] for x in numlist])