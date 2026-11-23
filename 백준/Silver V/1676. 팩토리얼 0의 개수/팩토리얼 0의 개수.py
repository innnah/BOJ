def multi(n, total, mulnum):
    if n < 2:
        return 1
    if mulnum > n:
        return total

    return multi(n, total * mulnum, mulnum + 1)

multiplier = 1
n = multi(int(input()), 1, 1)
cnt = 0

while True:
    divider = 10 ** multiplier
    
    if n % divider != 0:
        break

    cnt += 1
    multiplier += 1

print(cnt)