import sys

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

    return isPrime

l = sieve(100000)
while True:
    n = input().rstrip()
    if n == "0":
        break
    i, j = 0, 1
    maximum = -1
    while i < len(n):
        if l[int(n[i:j])]:
            maximum = max(maximum, int(n[i:j]))
        j += 1
        if (j - i > 5) or j >= len(n):
            i += 1
            j = i+1
    print(maximum)