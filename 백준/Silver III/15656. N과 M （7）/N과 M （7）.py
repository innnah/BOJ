n, m = map(int, input().split())
numlist = sorted(list(map(int, input().split())))

def pick(taken=[]):
    if len(taken) == m:
        tmp = taken.copy()
        return tmp

    ret = []
    for i in numlist:
        taken.append(i)
        a = pick(taken)
        if type(a[0]) == type([1,2,3]):
            ret += a
        else:
            ret += [a]
        del taken[-1]

    return ret

for a in pick():
    print(*a)