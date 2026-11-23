def getnums(n):
    if int(n[-1]) == 0:
        return [int(n)]
    ret = [int(n)]
    for i in range(int(n[-1])):
        l = getnums(n + str(i))
        for a in l:
            if type(a) == type(1):
                ret += list(map(int, l))
                break
            else:
                ret += list(map(int, a))
    return ret

l = []
for i in range(10):
    l += getnums(str(i))
l.sort()
n = int(input())
if n > 1023:
    print(-1)
else:
    print(l[n-1])