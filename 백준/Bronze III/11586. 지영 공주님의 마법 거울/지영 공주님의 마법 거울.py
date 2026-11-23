n = int(input())
l = [input() for _ in range(n)]
c = int(input())
if c == 1: 
    for i in l:
        print(i)
elif c == 2:
    for i in l:
        print(i[::-1])
else:
    for i in range(n-1, -1, -1):
        print(l[i])