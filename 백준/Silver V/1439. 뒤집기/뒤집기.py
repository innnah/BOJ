import sys
input = sys.stdin.readline
s = input().rstrip()
n = len(s)
s0, s1 = 0, 0
for i in range(1, n):
    if s[i-1] != s[i]:
        if s[i-1] == '0':
            s0 += 1
        else:
            s1 += 1
if s[-1] == '0':
    s0 += 1
else:
    s1 += 1
print(min(s0, s1))