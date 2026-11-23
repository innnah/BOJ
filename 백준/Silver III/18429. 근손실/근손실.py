import math

n, k = map(int, input().split())
numlist = list(map(int, input().split()))

def pick(taken, picked=[]):
    nums = [i for i in range(1, n+1)]
    if len(picked) == n:
        return picked

    ret = []
    for i in range(n):
        if not taken[i]:
            taken[i] = True
            if picked == []:
                tmp = pick(taken, picked+[nums[i]]).copy()
            else:
                tmp = pick(taken, picked+[nums[i]]).copy()
            try:
                if type(tmp[0]) == type([1,2,3]):
                    ret += tmp
                else:
                    ret.append(tmp)
            except:
                pass
            taken[i] = False

    return ret

def solve():
    cnt = math.factorial(n)
    nums = pick([False for _ in range(n)])
    for a in nums:
        muscle = 500
        for i in a:
            muscle += numlist[i-1] - k
            if muscle < 500:
                cnt -= 1
                break

    return cnt

print(solve())