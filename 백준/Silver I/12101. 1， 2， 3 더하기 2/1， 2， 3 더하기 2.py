def solve(target, s = 0, l = []):
    if target == s: return l
    if target < s: return []
    ret = []
    for i in range(1, 4):
        value = solve(target, s+i, l + [i])
        for j in value:
            if type(1) == type(j):
                ret.append(value)
            else:
                ret += value
            break

    return ret

n, k = map(int, input().split())
l = solve(n)
if k-1 < len(l):
    for i in l[k-1][:-1]:
        print(i, end = '+')
    print(l[k-1][-1])
else:
    print(-1)