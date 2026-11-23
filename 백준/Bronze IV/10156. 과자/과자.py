a, b, c = map(int, input().split())
lack = a * b - c

print(lack if lack > 0 else 0)