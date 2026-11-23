a, b = map(int, input().split())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

print(a * b // gcd(a, b))