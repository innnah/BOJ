l = list(sorted(map(int, input().split())))
if l[0]+l[1] == l[2]:
    print(1)
elif l[0]*l[1] == l[2]:
    print(2)
else:
    print(3)