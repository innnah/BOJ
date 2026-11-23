def changebase(num, k):
    ret = ""
    while num > 0:
        ret += str(num % k)
        num //= k
    return ret[::-1]

print(changebase(int(input()), 9))