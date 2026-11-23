n = int(input())
names = [input() for _ in range(n)]
original = names.copy()

names.sort()
if names == original:
    print("INCREASING")
    exit()
names.sort(reverse = True)
if names == original:
    print("DECREASING")
else:
    print("NEITHER")