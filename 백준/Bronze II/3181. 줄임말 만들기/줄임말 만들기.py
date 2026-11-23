l = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
s = input().split()
ret = s[0][0].upper()
for i in s[1:]:
    if i not in l:
        ret += i[0].upper()
print(ret)