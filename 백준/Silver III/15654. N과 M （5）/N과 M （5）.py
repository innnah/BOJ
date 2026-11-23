n, m = map(int, input().split())
numlist = sorted(list(map(int, input().split())))

def pick(taken = []):
    if len(taken) == m:
        return taken
    ret = []
    for x in numlist:
        if x not in taken:
            taken.append(x)
            ret += pick(taken)
            taken.remove(x)

    return ret  

result = pick()
for i in range(1, len(result)+1):
    if not i % m:
        print(result[i-1])
    else:
        print(result[i-1], end = ' ')