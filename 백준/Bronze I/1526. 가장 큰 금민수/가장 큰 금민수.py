n = int(input())
for i in range(n, -1, -1):
    si = str(i)
    for k in si:
        if k not in ('4', '7'):
            break
    else:
        print(i)
        break