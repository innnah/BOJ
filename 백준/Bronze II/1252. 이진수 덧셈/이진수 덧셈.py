a, b = map(int, input().split())

a = int('0b' + str(a), 2)
b = int('0b' + str(b), 2)

print(format(a + b, 'b'))