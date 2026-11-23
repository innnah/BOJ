n, m = map(int, input().split())
numlist = sorted(list(map(int, input().split())))

def pick(freq, taken=[False for _ in range(n)]):
    if len(freq) == m:
        tmp = freq.copy()
        return tmp
    
    ret = []
    for i in range(n):
        if len(freq) == 0:
            if not taken[i]:
                taken[i] = True
                a = pick(freq+[numlist[i]], taken)
                if len(a) != 0:
                    if type(a[0]) == type([1,2,3]):
                        ret += a
                    else:
                        ret += [a]
                taken[i] = False
        else:
            if not taken[i] and freq[-1] < numlist[i]:
                taken[i] = True
                a = pick(freq+[numlist[i]], taken)
                if len(a) != 0:
                    if type(a[0]) == type([1,2,3]):
                        ret += a
                    else:
                        ret += [a]
                taken[i] = False

    return ret

for a in pick([]):
    print(*a)