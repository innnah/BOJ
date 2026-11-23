n, m = map(int, input().split())

def pick(taken = []):
    if len(taken) == m:
        return taken
    ret = []
    for i in range(1, n+1):
        if i not in taken:
            taken.append(i)
            ret += pick(taken)
            taken.remove(i)

    return ret  

result = pick()
for i in range(1, len(result)+1):
    if not i % m:
        print(result[i-1])
    else:
        print(result[i-1], end = ' ')