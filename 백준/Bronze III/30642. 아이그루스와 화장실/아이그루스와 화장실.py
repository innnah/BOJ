n = int(input())
s = input()
k = int(input())
if s == 'induck':
    if k % 2 == 1:
        if k+1 > n:
            print(k-1)
        else:
            print(k+1)
    else:
        print(k)
else:
    if k % 2 == 0:
        if k+1 > n:
            print(k-1)
        else:
            print(k+1)
    else:
        print(k)