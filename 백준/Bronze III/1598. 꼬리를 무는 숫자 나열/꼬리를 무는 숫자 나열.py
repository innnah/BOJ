a, b = map(int, input().split())
a-=1
b-=1
v = abs(a%4-b%4)
h = abs(a//4-b//4)
print(h+v)