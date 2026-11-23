def power(x, y, mod):
    res = 1
    x %= mod
    while y:
        if y % 2:  res = (res * x) % mod
        y //= 2
        x = (x*x) % mod
    
    return res

def miller_rabin(n, a):
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d = d//2
    
        x = power(a, d, n)
        if x == 1 or x == n-1:
            return True
    
        for _ in range(r-1):
            x = power(x, 2, n)
            if x == n - 1:
                return True
            return False
 
def is_prime(n):
    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for a in alist:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            break

        n += 1