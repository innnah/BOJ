import sys
input = sys.stdin.readline
for _ in range(int(input())):
    y, k = 0, 0
    for _ in range(9):
        n, m = map(int, input().split())
        y += n
        k += m
    if y > k: print("Yonsei")
    elif y == k: print("Draw")
    else: print("Korea")