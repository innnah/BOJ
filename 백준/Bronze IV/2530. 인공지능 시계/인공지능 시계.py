h, m, s = map(int, input().split())
n = int(input())
s += n
tmp = s // 60
s %= 60
m += tmp
tmp = m // 60
m %= 60
h += tmp
h %= 24

print(h, m, s)