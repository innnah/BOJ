n = int(input())
m = int(input())
ret = m
a = [0, '-500', '*0.9', '-2000', '*0.75']
for i in range(5, 21, 5):
    if n >= i:
        ret = min(ret, max(0, int(eval(str(m)+a[i//5]))))
print(ret)