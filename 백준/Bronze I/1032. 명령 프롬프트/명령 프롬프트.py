n = int(input())

strings = [input() for _ in range(n)]
sRet = ""

for i in range(len(strings[0])):
    tmp = []
    for j in range(len(strings)):
        tmp.append(strings[j][i])

    if tmp.count(tmp[0]) == len(tmp):
        sRet += tmp[0]
    else:
        sRet += '?'

print(sRet)