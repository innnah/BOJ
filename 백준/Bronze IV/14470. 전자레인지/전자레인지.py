t = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
ret = 0
if t < 0:
    ret += -t * c
    t = 0
if t == 0:
    ret += d
ret += e * (b-t)
print(ret)