n = int(input())
names = [input()[0] for _ in range(n)]
a = list(set(names))
a.sort()
useable = ""

for i in a:
    if names.count(i) >= 5:
        useable += i

if useable == "":
    print("PREDAJA")
else:
    print(useable)