lv = 1
rv = 1

n = int(input())

def match(count, lv, rv):
    global n
    if n == 0:
        return 0
    if n < 3:
        return 1
    if count > n:
        return rv

    tmp = lv + rv

    lv = rv
    rv = tmp
    return match(count + 1, lv, rv)

print(match(3, lv, rv))