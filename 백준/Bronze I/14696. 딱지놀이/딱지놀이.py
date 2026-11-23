import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _, *a = list(map(int, input().split()))
    _, *b = list(map(int, input().split()))
    al, bl = [0 for _ in range(4)], [0 for _ in range(4)]
    for i in a: al[4-i] += 1
    for i in b: bl[4-i] += 1
    if al > bl: print("A")
    elif al < bl: print("B")
    else: print("D")