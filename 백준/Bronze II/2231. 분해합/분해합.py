n = int(input())

for i in range(n):
    listi = list(str(i))
    total = i

    for j in listi:
        total += int(j)

    if n == total:
        print(i)
        break
else:
    print(0)