def power(a, b, c):
    if b == 1: return a % c
    if b % 2 == 1: return (power(a, b-1, c) * (a%c)) % c
    ret = power(a, b//2, c)
    return (ret*ret) % c

a, b, c = map(int, input().split())
print(power(a, b, c))