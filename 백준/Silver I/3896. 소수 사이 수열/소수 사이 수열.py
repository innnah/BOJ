import sys, bisect

input = sys.stdin.readline

def sieve(n):
    isPrime = [True] * (n+1)
    isPrime[0] = False
    isPrime[1] = False

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if isPrime[i]:
            for j in range(i ** 2, n+1, i):
                isPrime[j] = False

    ret = []
    for i in range(n+1):
        if isPrime[i]:
            ret.append(i)
    return ret

l = sieve(1299709)
n = int(input())
for _ in range(n):
    i = int(input())
    if i in l:
        print(0)
        continue
    idx = bisect.bisect_left(l, i)
    print(l[idx] - l[idx-1])