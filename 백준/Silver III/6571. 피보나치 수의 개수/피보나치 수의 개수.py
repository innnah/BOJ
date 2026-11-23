import bisect
fib = [1, 2]
for i in range(2, 501):
    fib.append(fib[i-1] + fib[i-2])
    
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    print(bisect.bisect(fib, m) - bisect.bisect_left(fib, n))