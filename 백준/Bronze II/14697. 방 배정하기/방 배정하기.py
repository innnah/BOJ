import sys
input = sys.stdin.readline

a, b, c, s = list(map(int, input().split()))
for i in range(0, s+1, a):
    for j in range(0, s+1, b):
        for k in range(0, s+1, c):
            if i + j + k == s:
                print(1)
                sys.exit(0)
print(0)