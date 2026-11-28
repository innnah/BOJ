n = int(input())
m = int(input())
k = m
print(n)
print(m)
while m > 0:
    print(n*(m%10))
    m //= 10
print(n*k)