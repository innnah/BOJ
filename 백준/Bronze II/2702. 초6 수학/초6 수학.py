def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))