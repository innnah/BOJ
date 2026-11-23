a = [0,1,2,3]
for _ in range(int(input())):
    x, y = map(int, input().split())
    a[x], a[y] = a[y], a[x]
print(a.index(1))