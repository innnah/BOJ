l = [int(input()) for _ in range(10)]
print(sum(l)//10)
a = []
for i in range(10):
    a.append(l.count(l[i]))
maxa = max(a)
for i in range(10):
    if a[i] == maxa:
        print(l[i])
        break