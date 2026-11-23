while 1:
    a,b,c=input().split()
    if a == '#': break
    b=int(b)
    c=int(c)
    print(a,end=' ')
    if b > 17 or c >= 80:
        print('Senior')
    else:
        print('Junior')