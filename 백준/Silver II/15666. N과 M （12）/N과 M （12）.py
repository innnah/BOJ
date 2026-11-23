n, m = map(int, input().split())
numlist = sorted(list(set(map(int, input().split()))))

def pick(taken = []):
    if len(taken) == m:
        copied = taken.copy()
        return copied
    ret = []
    for x in numlist:
        try:
            if taken[-1] <= x:
                taken.append(x)
                sub = pick(taken)
                if type(sub[0]) == type([1,2,3]):
                    ret += sub
                else:
                    ret += [sub]
                taken.remove(x)
        except:
            taken.append(x)
            sub = pick(taken)
            if type(sub[0]) == type([1,2,3]):
                ret += sub
            else:
                ret += [sub]
            taken.remove(x)

    return ret

for i in pick():
    print(*i)