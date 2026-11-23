mod = 1000000007

def fibo(n):
    SIZE = 2
    ZERO = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]

    def square_matrix_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += ((a[i][k] % mod) * (b[k][j] % mod)) % mod

        return new
    
    def get_nth(n):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)

        return matrix

    return get_nth(n)[1][0]

n = int(input())
print(fibo(n) % mod)