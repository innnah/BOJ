import sys
input = sys.stdin.readline

while 1:
    s = input()
    if s == '': break
    n = int(s)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, 2*a+b
    print(b)