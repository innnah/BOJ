import sys
input = sys.stdin.readline

def query(v):
    ret = 0
    while v > 0:
        ret += tree[v]
        v -= (v & -v)
    return ret
def update(idx, num):
    while idx <= n:
        tree[idx] += num
        idx += (idx & -idx)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sarr = sorted(list(set(arr)))
    d = {sarr[i] : i for i in range(len(sarr))}
    arr = [d[i] for i in arr]

    tree = [0 for _ in range(n+1)]
    nums = [[[], 0, -1] for _ in range(len(sarr))]
    for i in range(n):
        nums[arr[i]][0].append(i)
    for i in range(len(sarr)):
        nums[i][2] = len(nums[i][0])-1
    ans = 0
    for i in range(len(sarr)-1, -1, -1):
        while nums[i][1] <= nums[i][2]:
            #print(nums[i])
            idx1 = nums[i][0][nums[i][1]]
            idx2 = nums[i][0][nums[i][2]]
            lcand = idx1 - query(idx1)
            rcand = n-1 - idx2 - (query(n) - query(idx2))
            #print(lcand, rcand, query(idx1), query(idx2), query(n))
            if lcand <= rcand:
                update(idx1+1, 1)
                nums[i][1] += 1
            else:
                update(idx2+1, 1)
                nums[i][2] -= 1
            ans += min(lcand, rcand)
    print(ans)