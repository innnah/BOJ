s = input()
a = set()
for i in range(len(s)):
    st = ""
    for j in range(i, len(s)):
        st += s[j]
        a.add(st)
print(len(a))