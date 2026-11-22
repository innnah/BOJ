tri = []
s = 0
add = 1
while s <= 1000:
    s += add
    tri.append(s)
    add += 1
for _ in range(int(input())):
    n = int(input())
    res = 0
    for i in range(len(tri)):
        for j in range(len(tri)):
            for k in range(len(tri)):
                if n == tri[i]+tri[j]+tri[k]:
                    res = 1
    print(res)