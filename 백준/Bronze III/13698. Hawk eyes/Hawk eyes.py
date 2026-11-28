s = input()
p = [0, 1, 2, 3]
for i in s:
    if i == 'A':
        p[0], p[1] = p[1], p[0]
    elif i == 'B':
        p[0], p[2] = p[2], p[0]
    elif i == 'C':
        p[0], p[3] = p[3], p[0]
    elif i == 'D':
        p[1], p[2] = p[2], p[1]
    elif i == 'E':
        p[1], p[3] = p[3], p[1]
    else:
        p[2], p[3] = p[3], p[2]
print(p.index(0)+1)
print(p.index(3)+1)