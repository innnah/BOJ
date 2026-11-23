l = list(map(int, input().split()))
for i in range(8):
    if l[i] not in (0, 1):
        print("F")
        break
else:
    print("S")