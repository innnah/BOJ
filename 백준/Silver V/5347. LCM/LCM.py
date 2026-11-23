def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return (a*b) // gcd(a,b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))