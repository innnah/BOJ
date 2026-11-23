numlist = list(map(int, input().split()))

numlist.remove(max(numlist))

print(max(numlist))