def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for _ in range(int(input())):
    numlist = list(map(int, input().split()))
    gcds = []
    for i in range(len(numlist)):
        for j in range(len(numlist)):
            if i == j:
                continue
            gcds.append(gcd(numlist[i], numlist[j]))
    print(max(gcds))