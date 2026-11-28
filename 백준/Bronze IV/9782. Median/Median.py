i = 1
while 1:
    _, *l = map(int, input().split())
    if l == []: break
    print(f"Case {i}: ", end='')
    if len(l) % 2:
        print(l[len(l)//2]/1)
    else:
        print((l[len(l)//2-1]+l[len(l)//2])/2)
    i += 1