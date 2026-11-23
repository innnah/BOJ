numlist = [int(input()) for _ in range(8)]
original = numlist.copy()
indexes = []
total = 0

for _ in range(5):
    indexes.append(original.index(max(numlist)) + 1)
    total += max(numlist)
    numlist.remove(max(numlist))

indexes.sort()

print(total)

for x in indexes:
    print(x, end = ' ')