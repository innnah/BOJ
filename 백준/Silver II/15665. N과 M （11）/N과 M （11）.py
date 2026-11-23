n, m = map(int, input().split())
numlist = list(set(map(int, input().split())))

numlist.sort()

def choose(numlist, m, freq = []):
    chosen = []

    if len(freq) == m:
        return freq

    for x in numlist:
        if len(freq) == 1:
            chosen += [choose(numlist, m, freq + [x])]
        else:
            chosen += choose(numlist, m, freq + [x])

    return chosen

ret = choose(numlist, m)
pointer = 0

for x in ret:
    try:
        for i in x:
            print(i, end = ' ')
        print()
    except:
        print(x)