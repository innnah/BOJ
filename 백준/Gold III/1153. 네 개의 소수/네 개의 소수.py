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

l = sieve(1000000)
n = int(input())
if n % 2:
    n -= 5
    if n < 4:
        print(-1)
    for i in range(n):
        if l[i] and l[n-i]:
            print(2,3,i,n-i)
            break
else:
    n -= 4
    if n < 4:
        print(-1)
    for i in range(n):
        if l[i] and l[n-i]:
            print(2,2,i,n-i)
            break