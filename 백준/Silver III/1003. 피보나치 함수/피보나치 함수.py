cache = [[1, 0], [0, 1]] + [[-1, -1] for _ in range(40)]

def fib(n):
    if n == 0 or n == 1:
        return cache[n]

    if cache[n] != [-1, -1]: return cache[n]

    sub1 = fib(n-1)
    sub2 = fib(n-2)

    cache[n] = [sub1[0]+sub2[0], sub1[1]+sub2[1]]

    return cache[n]

k = int(input())
for _ in range(k):
    n = int(input())
    print(*fib(n))