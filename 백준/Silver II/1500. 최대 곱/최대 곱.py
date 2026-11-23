n, k = map(int, input().split())

numlist = [n // k for _ in range(k)]

if n % k == 0:
    print(numlist[0] ** k)
else:
    result = 1
    for i in range(k - (n % k)):
        result *= numlist[i]

    for i in range(k - (n % k), k):
        result *= (numlist[i] + 1)

    print(result)