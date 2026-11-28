s1 = input()
s2 = input()
s = ""
for i in range(8):
    s += s1[i]
    s += s2[i]
while len(s) > 2:
    ss = ""
    for i in range(len(s)-1):
        ss += str((int(s[i]) + int(s[i+1])) % 10)
    s = ss
print(s)