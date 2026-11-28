n, m = map(int, input().split())
if n == 1:
    print(*[1 for _ in range(m)])
elif (n, m) == (2, 1):
    print(1, 2)
else:
    print(-1)