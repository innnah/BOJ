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

a, b = map(int, input().split())
c, d = map(int, input().split())

tmp1 = lcm(b, d)
tmp2 = [a * (tmp1 // b), c * (tmp1 // d)]
tmp3 = gcd(tmp2[0] + tmp2[1], tmp1)

if tmp3 != 1:
    result = [(tmp2[0] + tmp2[1]) // tmp3, tmp1 // tmp3]
else:
    result = [tmp2[0] + tmp2[1], tmp1]

print(int(result[0]), int(result[1]))