numlist = [int(input()) for _ in range(9)]

print(max(numlist))
print(numlist.index(max(numlist)) + 1)