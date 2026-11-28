import sys
sys.setrecursionlimit(40000)
input = sys.stdin.readline

def bitcount(used):
    cnt = 0
    for i in range(10):
        cnt += bool(used & (1<<i))
    return cnt

def dpf(d, used, big):
    if d == 0:
        return (bitcount(used) == k, 0)
    if dp[d][used][big] != (-1, 0): return dp[d][used][big]
    #print(d, used, big)
    if big:
        for i in range(10):
            pos, val = dpf(d-1, used | (1 << i), 1)
            if pos:
                dp[d][used][1] = (1, i*(10**(d-1))+val)
                return dp[d][used][1]
    else:
        s = n[d-1]
        if not used and s == 0:
            pos, val = dpf(d-1, 0, 0)
        else:
            pos, val = dpf(d-1, used | (1 << s), 0)
        if pos:
            dp[d][used][0] = (1, s*(10**(d-1))+val)
            return dp[d][used][0]
        for i in range(s+1, 10):
            pos, val = dpf(d-1, used | (1 << i), 1)
            if pos:
                dp[d][used][0] = (1, i*(10**(d-1))+val)
                return dp[d][used][0]

    dp[d][used][big] = (0, 0)
    return (0, 0)

n, k = map(int, input().split())
n = list(map(int, str(n)))[::-1]
l = len(n)
n += [0 for _ in range(20)]

dp = [[[(-1, 0), (-1, 0)] for _ in range(1<<10)] for _ in range(30)]

pos, val = dpf(l+9, 0, 0)
print(val)