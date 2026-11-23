k,d,a=map(int,input().split('/'))
if d == 0: print('hasu')
else:
    print('gosu' if k+a>=d else 'hasu')