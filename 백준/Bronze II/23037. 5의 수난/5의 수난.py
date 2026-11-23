l = list(map(int, list(input())))
ret = 0
for i in l:
    ret += i ** 5
print(ret)