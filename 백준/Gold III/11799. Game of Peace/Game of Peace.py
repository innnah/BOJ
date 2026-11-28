import sys, math
input = sys.stdin.readline

for c in range(int(input())):
    x, n, y, m = map(int, input().split())
    a, b = x, 0
    for i in range(n):
        a, b = a+b, a
    a += y
    print(f"Case {c+1}: {math.gcd(a, b)}")