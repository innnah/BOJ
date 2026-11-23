def changebase(num, k):
    ret = []
    while abs(num) > 0:
        ret.append(num%k)
        num //= k
    return ret[::-1]
for i in range(1000, 10000):
    a, b, c = sum(changebase(i, 10)), sum(changebase(i, 12)), sum(changebase(i, 16))
    if a == b and b == c:
        print(i)