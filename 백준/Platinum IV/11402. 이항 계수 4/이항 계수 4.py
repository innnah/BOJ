def bino2(n, k, m):
    binomial = [[0] * (m+10) for _ in range(m+10)]
    for i in range(m):
        binomial[i][0] = 1
        for j in range(1, i+1):
            binomial[i][j] = (binomial[i-1][j-1] + binomial[i-1][j]) % m
    ret = 1
    while (n or k):
        ret *= binomial[n%m][k%m]
        n //= m
        k //= m
        ret %= m
    return ret

n, k, m = map(int, input().split())
print(bino2(n, k, m))