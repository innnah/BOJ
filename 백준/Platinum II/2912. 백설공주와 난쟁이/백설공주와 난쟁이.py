import sys, random, bisect
input = sys.stdin.readline

n, m = map(int, input().split())
k = 100
arr = list(map(int, input().split()))
nums = [[] for _ in range(m+1)]
for i in range(n):
    nums[arr[i]].append(i)
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    ans = -1
    for _ in range(k):
        rnd = random.randint(a, b) - 1
        num = arr[rnd]
        bs = bisect.bisect(nums[num], b-1) - bisect.bisect_left(nums[num], a-1)
        if bs > (b-a+1)//2:
            ans = num
            break
    if ans == -1:
        print("no")
    else:
        print(f"yes {ans}")