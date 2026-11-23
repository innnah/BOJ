l, a, b, c, d = (int(input()) for _ in range(5))
korean = a // c + 1 if a % c else a // c
math = b // d + 1 if b % d else b // d
print(l - (max(korean, math)))