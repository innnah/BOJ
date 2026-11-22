import sys
input = sys.stdin.readline

def strength(a):
    if a == 2: return 1
    for i in range(1, a+1):
        if a % i:
            return strength(i)+1
    return 1

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b//gcd(a, b)

s, e = map(int, input().split())
result = 0
remain = e-s+1
divisor = 1
i = 1
prev = e-s+1
while remain > 0:
    l = (s+(divisor-1)) // divisor
    r = e // divisor
    remain = r-l+1
    result += (strength(i)+1)*(prev-remain)
    i += 1
    divisor = lcm(i, divisor)
    prev = remain
print(result)