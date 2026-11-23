MOD = 10**9+7
def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += A[i][k] * B[k][j] % MOD
    return temp

n = int(input())
mul = [[4,-1],[1,0]]
ret = [[1,0],[0,1]]
init = [[1,0],[1,0]]
if n%2:
    print(0)
else:
    n //= 2
    while n:
        if n % 2:
            ret = matrix_mult(ret, mul)
        mul = matrix_mult(mul, mul)
        n //= 2
    ret = matrix_mult(ret, init)
    print(ret[0][0] % MOD)