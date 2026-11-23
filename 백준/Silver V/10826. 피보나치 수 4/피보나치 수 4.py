def fib_f(n):
    if n == 0:
        return 0
        
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a

print(fib_f(int(input())))