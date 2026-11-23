n, m = map(int, input().split())
numlist = list(map(int, input().split()))

def pick(taken, a=[]):
    if len(a) == m:
        return tuple(a)
    ret = []
    for i in range(n):
        if a != []:
            if not taken[i] and numlist[i] >= a[-1]:
                taken[i] = True
                tmp = pick(taken, a + [numlist[i]])
                try:
                    if type(tmp[0]) == type((1,2,3)):
                        ret += list(tmp)
                    else:
                        ret.append(tmp)
                except:
                    pass
                taken[i] = False
        else:
            if not taken[i]:
                taken[i] = True
                tmp = pick(taken, a + [numlist[i]])
                try:
                    if type(tmp[0]) == type((1,2,3)):
                        ret += list(tmp)
                    else:
                        ret.append(tmp)
                except:
                    pass
                taken[i] = False

    return ret

for i in sorted(list(set(pick([False for _ in range(n)])))):
    tmp = list(i)
    print(*i)