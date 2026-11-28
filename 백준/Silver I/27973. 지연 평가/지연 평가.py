import sys
input = sys.stdin.readline

start, end, step = 1, 1234567890123, 1
for _ in range(int(input())):
    l = list(map(int, input().split()))
    a, b = 0, 0
    if len(l) == 1:
        a = 3
    else:
        a, b = l
    if a == 0:
        start += b
        end += b
    elif a == 1:
        start *= b
        end *= b
        step *= b
    elif a == 2:
        start += step*b
    else:
        print(start)