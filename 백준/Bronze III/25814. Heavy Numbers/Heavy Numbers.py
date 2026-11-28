a, b = input().split()
va = len(a) * sum(map(int, a))
vb = len(b) * sum(map(int, b))
if va > vb:
    print(1)
elif va < vb:
    print(2)
else:
    print(0)