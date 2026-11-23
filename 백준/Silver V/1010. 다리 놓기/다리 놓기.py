from math import factorial
for _ in range(int(input())):
    a, b = map(int, input().split())
    n = max(a, b)
    r = min(a, b)
    print(factorial(n) // (factorial(n-r) * factorial(r)))