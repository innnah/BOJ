n, m = map(int, input().split())
chars = input().rstrip().split()

chars.sort()

def makePassword(charlist, length, **others):
    taken = others['taken']
    firstFree = others['last'] + 1

    if length == 0:
        password = ''
        for x in range(len(taken)):
            if taken[x]:
                password += charlist[x]
        
        return [password]

    tmp = []

    for i in range(firstFree, len(taken)):
        taken[i] = True
        tmp += makePassword(charlist, length - 1, taken = taken, last = i)
        taken[i] = False

    return tmp

ret = makePassword(chars, n, taken = [False for _ in range(m)], last = -1)
words = ['a', 'e', 'i', 'o', 'u']

ret.sort()

for x in ret:
    cnt = 0
    for a in words:
        cnt += x.count(a)
    if cnt == 0:
        continue
    elif n - cnt < 2:
        continue

    print(x)