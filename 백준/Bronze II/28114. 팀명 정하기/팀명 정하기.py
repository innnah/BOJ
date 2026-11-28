a = [input().split() for _ in range(3)]
for i in range(3):
    a[i][0] = int(a[i][0])
    a[i][1] = int(a[i][1])
a.sort(key = lambda x : x[1])
print(f"{a[0][1]%100}{a[1][1]%100}{a[2][1]%100}")
a.sort(reverse = True)
print(f"{a[0][2][0]}{a[1][2][0]}{a[2][2][0]}")