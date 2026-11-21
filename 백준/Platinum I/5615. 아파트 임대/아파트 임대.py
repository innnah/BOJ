import sys
input = sys.stdin.readline

def miller_rabin(n, a):
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d = d//2
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return 1
    for _ in range(r-1):
        x = pow(x, 2, n)
        if x == n-1:
            return 1
    return 0
 
def is_prime(n):
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0:
        return 0
    for i in a:
        if n == i:
            return 1
        if not miller_rabin(n, i):
            return 0
    return 1

ret = 0
for _ in range(int(input())):
    n = int(input())
    if is_prime(n*2+1): ret += 1
print(ret)