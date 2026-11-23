import math

n = int(input())
numlist = list(map(int, input().split()))
cnt = 0

def isPrime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False

    if n < 4:
        return True

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

for i in numlist:
    if isPrime(i):
        cnt += 1

print(cnt)