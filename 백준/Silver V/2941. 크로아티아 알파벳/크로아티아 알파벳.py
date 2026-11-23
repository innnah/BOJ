alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input().rstrip()
length = len(s)
cnt = 0
dz = 0

for x in alpa:
    tmp = s.count(x)
    if x != "dz=" and x != "z=":
        cnt += tmp
        length -= tmp * len(x)
    elif x == "dz=":
        cnt += tmp
        dz = tmp
        length -= tmp * len(x)
    else:
        cnt += tmp - dz
        length -= (tmp - dz) * len(x)
        
print(cnt + length)