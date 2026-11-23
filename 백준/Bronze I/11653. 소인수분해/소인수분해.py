def factor(n, ret = ""):
    if n == 1 and ret == "":
        return "1"
    elif n == 1 and ret != "":
        return ret
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return factor(n // i, ret + str(i) + " ")
        else:
            return ret + str(n)

numlist = list(map(int, factor(int(input())).split()))

for x in numlist:
    if x != 1:
        print(x)