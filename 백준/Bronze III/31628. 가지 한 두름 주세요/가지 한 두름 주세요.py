arr = [input().split() for _ in range(10)]
for i in range(10):
    for j in range(10):
        if arr[i][0] != arr[i][j]:
            break
    else:
        print(1)
        exit(0)
    for j in range(10):
        if arr[0][i] != arr[j][i]:
            break
    else:
        print(1)
        exit(0)
print(0)