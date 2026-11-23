ret = 0
for _ in range(int(input())):
    s = int(input()[2:])
    if s <= 90: ret += 1
print(ret)