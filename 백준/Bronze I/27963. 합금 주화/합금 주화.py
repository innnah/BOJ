import sys
input = sys.stdin.readline

a, b, x = map(int, input().split())
if a < b:
    a, b = b, a
w1, w2 = a, a * (100-x)/x
s1, s2 = 1, w2/b
print((w1+w2) / (s1+s2))