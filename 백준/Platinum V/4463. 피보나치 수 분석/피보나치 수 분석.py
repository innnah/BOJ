import sys, random, bisect, math

sys.setrecursionlimit(100000)
input = sys.stdin.readline

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x*x) % p
    return res
 
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
 
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
 
 
def pollardRho(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollardRho(n)
    if is_prime(d):
        return d
    else:
        return pollardRho(d)

def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])
    return temp

def matrix_pow(n):
    matrix = [[1, 0], [0, 1]]
    k = 0
    tmp = [[1, 1], [1, 0]]

    while 2 ** k <= n:
        if n & (1 << k) != 0:
            matrix = matrix_mult(matrix, tmp)
        k += 1
        tmp = matrix_mult(tmp, tmp)

    return matrix

def fib2(n):
    if n == 0: return 0
    return matrix_pow(n-1)[0][0]

fib = [0] * 93
for i in range(93):
    fib[i] = fib2(i)

while True:
    try:
        n, m = input().split()
        n = int(n, 16)
        m = int(m, 16)
    except:
        break
    if n >= m: break
    print(f"Range {n} to {m}:")
    idx1 = bisect.bisect_left(fib, n)
    idx2 = bisect.bisect(fib, m)
    if idx1 == idx2:
        print("No Fibonacci numbers in the range")
        print()
        continue
    for i in range(idx1, idx2):
        print(f"Fib({i}) = {fib[i]},", end = ' ')
        if i != 0:
            print(f"lg is {math.log2(fib[i]):.6f}")
        else:
            print("lg does not exist")
        if i <= 2:
            print("No prime factors")
        elif is_prime(fib[i]):
            print(f"Prime factors: {fib[i]}")
        else:
            numlist = []
            a = fib[i]
            while a > 1:
                divisor = pollardRho(a)
                numlist.append(divisor)
                a = a // divisor
            numlist.sort()
            print("Prime factors: ", end = '')
            print(*numlist)
    print()