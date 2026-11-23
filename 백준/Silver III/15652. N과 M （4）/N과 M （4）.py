n, m = map(int, input().split())

def pick(taken = []):
    if len(taken) == m:
        copied = taken.copy()
        return copied
    ret = []
    for i in range(1, n+1):
        try:
            if taken[-1] <= i:
                taken.append(i)
                tmp = pick(taken)
                if type(tmp[0]) == type([10,11,12]):
                    ret += tmp
                else:
                    ret += [tmp]
                del taken[-1]
        except:
            taken.append(i)
            tmp = pick(taken)
            if type(tmp[0]) == type([10,11,12]):
                ret += tmp
            else:
                ret += [tmp]
            del taken[-1]

    return ret

for i in pick():
    print(*i)