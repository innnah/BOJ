import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
w = [1, complex(-0.5, 1), complex(-0.5, -1)]
s = complex(0, 0)
for i in l:
    s += w[i%3]
print(s.imag, end = ' ')
print(0.5 * s.imag + s.real)