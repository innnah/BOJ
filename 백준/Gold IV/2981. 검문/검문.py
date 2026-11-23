import math

n = int(input())
l = [int(input()) for _ in range(n)]

def gcd(l):
    def gcd2(a, b):
        while b != 0:
            a, b = b, a%b
        return a
    
    ret = l[0]
    for i in range(1, len(l)):
        ret = gcd2(ret, l[i])
    return ret

subList = []
for i in range(1, len(l)):
    subList.append(abs(l[i-1] - l[i]))

m = gcd(subList)
cache = []
for i in range(2, int(math.sqrt(m)) + 1):
    if m % i == 0:
        cache.append(i)
        print(i, end = ' ')
for i in cache[::-1]:
    if m // i not in cache:
        print(m // i, end = ' ')
print(m, end = ' ')