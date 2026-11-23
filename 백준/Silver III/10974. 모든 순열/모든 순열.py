n = int(input())

def pick(n, picked, l=[]):
    if all(picked):
        return l
    else:
        ret = []
        for i in range(n):
            if not picked[i]:
                picked[i] = True
                tmp = pick(n, picked, l + [i+1]).copy()
                if type(tmp[0]) == type([1,2,3]):
                    ret += tmp
                else:
                    ret.append(tmp)
                picked[i] = False

        return ret

for i in pick(n, [False for _ in range(n)]):
    print(*i)