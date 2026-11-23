import sys, math
input = sys.stdin.readline

def dp(num, visited):
    if visited == (1 << n) - 1:
        return num % k == 0
    ret = cache[num][visited]
    if ret != -1: return ret
    ret = 0
    for i in range(n):
        if visited & (1 << i): continue
        newnum = rm[num][c[i]] + nums[i]
        newnum %= k
        v = dp(newnum, visited + (1 << i))
        ret += v
    cache[num][visited] = ret
    return ret

n = int(input())
nums = [int(input()) for _ in range(n)]
k = int(input())
c = []
for i in range(n):
    c.append(len(str(nums[i])))
max_c = max(c)
rm = [[0] * (max_c+1) for _ in range(k)]
for i in range(k):
    for j in range(max_c+1):
        rm[i][j] = i * 10 ** j
cache = [[-1] * (1 << n) for _ in range(k)]
ret = dp(0, 0)
fact = math.factorial(n)
g = math.gcd(ret, fact)
print(f"{ret//g}/{fact//g}")