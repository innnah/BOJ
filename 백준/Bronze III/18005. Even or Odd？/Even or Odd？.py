n = int(input())
if n % 2:
    print(0)
else:
    s = n*(n+1)//2
    if s % 2: print(1)
    else: print(2)