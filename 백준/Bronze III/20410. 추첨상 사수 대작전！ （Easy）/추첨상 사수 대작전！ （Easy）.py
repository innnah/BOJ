m, seed, x1, x2 = map(int, input().split())
for a in range(m):
    for c in range(m):
        nx1 = (a*seed+c) % m
        nx2 = (a*nx1+c) % m
        if nx1 == x1 and nx2 == x2:
            print(a, c)
            exit(0)