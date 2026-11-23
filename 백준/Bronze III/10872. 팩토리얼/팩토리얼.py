def multi(n, total, mulnum):
    if n < 2:
        return 1
    if mulnum > n:
        return total

    return multi(n, total * mulnum, mulnum + 1)

print(multi(int(input()), 1, 1))