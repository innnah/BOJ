n, m = map(int, input().split())

def pick(taken = []):
    if len(taken) == m:
        copied = taken.copy()
        return copied
    ret = []
    for i in range(1, n+1):
        if len(taken) == 0:
            taken.append(i)
            tmp = pick(taken).copy()
            try:
                if type(tmp[0]) == type([1,2,3]):
                    ret += tmp
                else:
                    ret += [tmp]
            except:
                pass
            taken.remove(i)
        else:
            if taken[-1] < i:
                taken.append(i)
                tmp = pick(taken).copy()
                try:
                    if type(tmp[0]) == type([1,2,3]):
                        ret += tmp
                    else:
                        ret += [tmp]
                except:
                    pass
                taken.remove(i)
    return ret

for i in pick():
    print(*i)