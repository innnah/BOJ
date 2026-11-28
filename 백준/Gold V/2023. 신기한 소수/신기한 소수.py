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

n = int(input())

def find(num, remain):
    numlist = []
    if remain == 1:
        if num != 0:
            for i in range(1, 10, 2):
                a = num * 10 + i
                if is_prime(a):
                    numlist.append(a)
        else:
            return [2,3,5,7]

    if num == 0:
        for i in [2,3,5,7]:
            numlist += (find(num * 10 + i, remain-1))
    else:
        for i in range(1, 10, 2):
            a = num * 10 + i
            if is_prime(a):
                numlist += (find(a, remain-1))

    return numlist

numlist = find(0, n)
for i in numlist:
    print(i)