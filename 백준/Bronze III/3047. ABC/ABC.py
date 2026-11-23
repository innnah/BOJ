l = sorted(list(map(int, input().split())))
a, b, c = l
s = input()
for i in s:
    if i == 'A': print(a, end = ' ')
    if i == 'B': print(b, end = ' ')
    if i == 'C': print(c, end = ' ')