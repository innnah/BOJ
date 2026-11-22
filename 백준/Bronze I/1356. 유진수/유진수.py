s = input()
for i in range(1, len(s)):
    a, b = list(map(int, s[:i])), list(map(int, s[i:]))
    am, bm = 1, 1
    for j in a:
        am *= j
    for j in b:
        bm *= j
    if am == bm:
        print("YES")
        break
else:
    print("NO")