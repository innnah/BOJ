def gcd(a, b):
    if a < b: a, b = b, a
    while b != 0:
        a, b = b, a%b

    return a

n = int(input())
for _ in range(n):
    ret = 0
    l = list(map(int, input().split()))
    k = l[0]
    l = l[1:]
    for i in range(k):
        for j in range(i+1, k):
            ret += gcd(l[i], l[j])
    print(ret)