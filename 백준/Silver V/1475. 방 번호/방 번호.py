l = [[0] * 10 for _ in range(7)]
s = input()
m = 0
for i in s:
    if i in ('6','9'):
        for j in range(7):
            if not l[j][6]:
                l[j][6] = 1
                m = max(m, j)
                break
            elif not l[j][9]:
                l[j][9] = 1
                m = max(m, j)
                break
    else:
        for j in range(7):
            if not l[j][int(i)]: 
                m = max(m, j)
                l[j][int(i)] = 1
                break
print(m+1)