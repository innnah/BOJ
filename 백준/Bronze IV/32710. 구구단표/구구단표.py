n = int(input())
arr = []
for i in range(2, 10):
    for j in range(1, 10):
        arr.append(i)
        arr.append(j)
        arr.append(i*j)
print(int(n in arr))