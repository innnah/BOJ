n = int(input())
i = 11
num = 2
if n == 1:
    print(1)
elif not n%2 or not n%5:
    print(-1)
else:
    while i % n:
        i %= n
        i = i * 10 + 1
        num += 1
    print(num)